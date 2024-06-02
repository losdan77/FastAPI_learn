from httpx import AsyncClient
import pytest

#@pytest.mark.asyncio
@pytest.mark.parametrize('email,password,role,status_code', [
    ('losdan322@gmail.com', '12345', 'admin', 200),
    ('maks@mail.ru', '12345', '', 200),
    ('test@test.com', '12345', '', 409),
])
async def test_register_user(email, 
                             password, 
                             role, 
                             status_code,
                             ac: AsyncClient):
    response = await ac.post('/auth/register', json={
        'email': email,
        'password': password,
        'role': role,
    })    

    assert response.status_code == status_code


@pytest.mark.parametrize('email,password,status_code', [
    ('losdan322@gmail.com', '12345', 200),
    ('test@test.com', 'test', 200),
    ('test_error@mail.ru', '12345', 401),
])
async def test_login_user(email, 
                          password, 
                          status_code,
                          ac: AsyncClient):
    response = await ac.post('/auth/login', json={
        'email': email,
        'password': password,
    })

    assert response.status_code == status_code