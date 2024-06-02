import pytest

from app.users.dao import UsersDAO

@pytest.mark.parametrize('id,email,is_present', [
    (1,'test@test.com', True),
    (3,'losdan322@gmail.com', True),
    (100,'error@mail.ru', False)
])
async def test_find_user_by_Id(id, email, is_present):
    user = await UsersDAO.find_by_id(id)

    if is_present:
        assert id == user.id
        assert email == user.email
    else:
        assert not user