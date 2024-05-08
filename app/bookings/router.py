from fastapi import APIRouter

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking


router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings() -> list[SBooking]:
    return await BookingsDAO.find_all()