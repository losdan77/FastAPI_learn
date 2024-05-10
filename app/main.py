#uvicorn main:app --reload
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel
from datetime import date

from app.bookings.router import router as router_bookings
from app.users.router import router as rouser_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms

app = FastAPI(title='Tranding App')

app.include_router(rouser_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)


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
