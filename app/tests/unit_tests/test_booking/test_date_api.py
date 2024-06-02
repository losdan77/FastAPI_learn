import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('room_id,date_from,date_to,status_code', [
    (2, '2002-10-10', '2002-10-20', 200),
    (2, '2002-10-10', '2002-10-05', 400),
])
async def test_date_add_booking_api(room_id,
                                    date_from,
                                    date_to,
                                    status_code,
                                    authontificated_ac: AsyncClient):
    response = await authontificated_ac.post('/bookings/add', params={
        'room_id': room_id,
        'date_from': date_from,
        'date_to': date_to,     
    })

    assert response.status_code == status_code


