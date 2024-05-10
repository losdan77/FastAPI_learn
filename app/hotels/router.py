from fastapi import APIRouter

from app.hotels.dao import HotelsDAO

router = APIRouter(
    prefix='/hotels',
    tags=['Отели'],
)


@router.get('')
async def get_hotels():
    return await HotelsDAO.find_all()