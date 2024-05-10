from fastapi import HTTPException, status

ExistingUserExeption = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Этот Email уже зарегестрирован',   
)

UncorectEmailOrPasswordExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Неверный email или пароль',
)

NoTokenExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Отсутсвует токен',
)

UncorectTokenExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Неправильный токен',
)

ExpireTokenExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Время действия токена истекло',
)

RoomCannotBeBooked = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Не осталось свободных номеров',   
)