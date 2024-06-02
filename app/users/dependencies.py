from fastapi import Request, Depends
from jose import jwt, JWTError
from datetime import datetime, timezone

from app.config import settings
from app.users.dao import UsersDAO
from app.exeptions import NoTokenExeption, UncorectTokenExeption, ExpireTokenExeption

def get_token(request: Request):
    try:
        token = request.cookies['booking_access_token']
    #if not token:
    except:
        raise NoTokenExeption
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_WORD, settings.HASH_ALGORITHM
        )
    except JWTError:
        raise UncorectTokenExeption
    
    expire: str = payload['exp']
    if (not expire) or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise ExpireTokenExeption
    
    user_id: str = payload['sub']
    if not user_id:
        raise UncorectTokenExeption
    
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UncorectTokenExeption
    
    #user = user['Users']
    user_dict = {'id': user.id,
                 'email': user.email}

    return user_dict