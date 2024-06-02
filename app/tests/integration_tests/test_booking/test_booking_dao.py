from datetime import datetime

from app.bookings.dao import BookingsDAO


async def test_add_booking():
    new_booking = await BookingsDAO.add(
        2,
        2,
        datetime.strptime('2024-10-10', '%Y-%m-%d'),
        datetime.strptime('2024-10-15', '%Y-%m-%d'),
    )

    check_new_booking = await BookingsDAO.find_all(
        user_id = 2,
        room_id = 2,
        date_from = datetime.strptime('2024-10-10', '%Y-%m-%d'),
        date_to = datetime.strptime('2024-10-15', '%Y-%m-%d'),
    )
    
    assert new_booking.id == check_new_booking[0].id


async def test_crud_booking():
    new_booking = await BookingsDAO.add(
        2,
        2,
        datetime.strptime('2007-10-10', '%Y-%m-%d'),
        datetime.strptime('2007-10-15', '%Y-%m-%d'),
    )
    added_booking_id = new_booking.id

    check_new_booking = await BookingsDAO.find_one_or_none(id=added_booking_id)
    assert check_new_booking != None

    await BookingsDAO.delete(added_booking_id, 2)

    check_new_booking = await BookingsDAO.find_one_or_none(id=added_booking_id)
    assert check_new_booking == None