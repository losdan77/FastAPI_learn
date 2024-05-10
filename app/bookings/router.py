from fastapi import APIRouter, Depends
from datetime import date

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking
from app.users.models import Users
from app.users.dependencies import get_current_user
from app.exeptions import RoomCannotBeBooked


router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)): #-> list[SBooking]:
    return await BookingsDAO.find_all(user_id = user['id'])


@router.post('/add')
async def add_bookings(room_id: int,
                       date_from: date,
                       date_to: date,
                       user: Users = Depends(get_current_user),):
    booking = await BookingsDAO.add(user['id'], room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked
