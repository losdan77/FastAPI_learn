import sentry_sdk
from prometheus_fastapi_instrumentator import Instrumentator

from contextlib import asynccontextmanager

from fastapi import FastAPI, Query, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date
import asyncio

from app.config import settings

from app.bookings.router import router as router_bookings
from app.users.router import router as rouser_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms

from app.imports.router import router as router_import

from app.pages.router import router as router_pages
from app.images.router import router as router_images

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from sqladmin import Admin
from app.admin.auth import authentication_backend
from app.database import engine_nullpool
from app.admin.view import UserAdmin, BookingAdmin, HotelsAdmin, RoomsAdmin

from app.logger import logger
import time

async def get_cache():
    '''Функция для постоянного выполнения фоновых задач,
    в асинхронном режиме'''
    while True:
        print('all correct!')
        await asyncio.sleep(60*5)


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}')
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    asyncio.create_task(get_cache())
    yield


sentry_sdk.init(
    dsn=settings.SENTRY_URL,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
) 


app = FastAPI(title='Tranding App', lifespan=lifespan)

app.mount('/static', StaticFiles(directory='app/static'), 'static')


instrumentator = Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=['.*admin.*', '/metrics'],
)
instrumentator.instrument(app).expose(app)


app.include_router(rouser_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)

app.include_router(router_import)

app.include_router(router_pages)
app.include_router(router_images)


@app.get('/')
def hello() -> str:
    return 'hi wirld'

# class Hotels_args():
#     def __init__(self,
#         hotel_area: str, 
#         date_start: date, 
#         date_end: date,
#         spa: bool = Query(None), 
#         stars: int = Query(None, ge=1, le=5),):

#         self.hotel_area = hotel_area
#         self.date_start = date_start
#         self.date_end = date_end 
#         self.spa = spa
#         self.stars = stars


# @app.get('/hotels/{hotel_area}')
# def hotels(search_args: Hotels_args = Depends()):
    
#     return search_args


admin = Admin(app, engine_nullpool, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
admin.add_view(BookingAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)


origins = [
    'http://localhost:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Content-Type',
                   'Set-Cookie',
                   'Access-Control-Allow-Headers',
                   'Access-Control-Allow-Origin',
                   'Authorization'],
)

@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info('Request handling time', extra={
        'process_time': round(process_time, 4)
    })
    return response
