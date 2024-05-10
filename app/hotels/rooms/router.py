from fastapi import APIRouter

from app.hotels.rooms.dao import RoomsDAO

router = APIRouter(
    prefix='/hotels',
    tags=['Hомера'],
)


@router.get('/{hotel_id}/rooms')
async def get_hotels(hotel_id: int):
    return await RoomsDAO.find_all(hotel_id=hotel_id)