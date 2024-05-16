#uvicorn main:app --reload
from fastapi import FastAPI, Query, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date

from app.bookings.router import router as router_bookings
from app.users.router import router as rouser_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms

from app.pages.router import router as router_pages
from app.images.router import router as router_images

app = FastAPI(title='Tranding App')

app.mount('/static', StaticFiles(directory='app/static'), 'static')

app.include_router(rouser_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)

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