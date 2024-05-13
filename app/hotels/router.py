from fastapi import APIRouter
from datetime import date

from app.hotels.dao import HotelsDAO

router = APIRouter(
    prefix='/hotels',
    tags=['Отели'],
)


@router.get('/{location}')
async def get_hotels_by_location(location: str, 
                                 date_from: date,
                                 date_to: date):
    return await HotelsDAO.find_all_by_location_with_rooms_left(location = location,
                                                                date_from = date_from,
                                                                date_to = date_to) 


@router.get('/id/{hotel_id}')
async def get_hotels(hotel_id: int):
    return await HotelsDAO.find_all(id = hotel_id)


@router.get('/{id}/rooms')
async def get_all_rooms_in_hotel_by_Id(id: int,
                                       date_from: date,
                                       date_to: date):
    return await HotelsDAO.find_all_rooms_in_hotel_by_id(id = id,       
                                                         date_from = date_from,
                                                         date_to = date_to)



