from app.dao.base import BaseDAO
from app.hotels.models import Rooms


class RoomsDAO(BaseDAO):
    model = Rooms