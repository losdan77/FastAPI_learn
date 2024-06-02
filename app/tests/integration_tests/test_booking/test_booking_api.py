import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('room_id,date_from,date_to,booking_count,status_code', [
    (4, '2025-10-10', '2025-10-15', 3, 200),
    (4, '2025-10-10', '2025-10-15', 4, 200),
    (4, '2025-10-10', '2025-10-15', 5, 200),
    (4, '2025-10-10', '2025-10-15', 6, 200),
    (4, '2025-10-10', '2025-10-15', 7, 200),
    (4, '2025-10-10', '2025-10-15', 8, 200),
    (4, '2025-10-10', '2025-10-15', 9, 200),
    (4, '2025-10-10', '2025-10-15', 10, 200),
    (4, '2025-10-10', '2025-10-15', 10, 409),
    (4, '2025-10-10', '2025-10-15', 10, 409),
])
async def test_api_add_and_get_booking(room_id,
                               date_from,
                               date_to,
                               booking_count,
                               status_code,
                               authontificated_ac: AsyncClient):
    response = await authontificated_ac.post('bookings/add', params={
        'room_id': room_id,
        'date_from': date_from,
        'date_to': date_to,
    })

    assert response.status_code == status_code

    response = await authontificated_ac.get('/bookings')
    assert len(response.json()) == booking_count


async def test_get_delete_and_get_all_booking(authontificated_ac: AsyncClient):
    response_get = await authontificated_ac.get('/bookings')
    bookings_json = response_get.json()
    assert len(bookings_json) > 0
    
    for booking in bookings_json:
        await authontificated_ac.delete(f'bookings/{booking["id"]}')

    response_get = await authontificated_ac.get('/bookings')
    bookings_json = response_get.json()
    assert len(bookings_json) == 0    