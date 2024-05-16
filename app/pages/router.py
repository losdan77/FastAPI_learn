from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.hotels.router import get_hotels_by_location

router = APIRouter(
    prefix='/pages',
    tags=['frontend']
)

templates = Jinja2Templates(directory='app/templates')

@router.get('/hotels')
async def get_hotels_page(request: Request,
                          hotels=Depends(get_hotels_by_location)):

    # hotels= await get_hotels_by_location('Республика',
    #                                      '2023-06-10',
    #                                      '2023-06-30')

    return templates.TemplateResponse(name='hotels.html',
                                      context={'request': request,
                                               'hotels': hotels})

