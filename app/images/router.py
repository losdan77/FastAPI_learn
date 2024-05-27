from fastapi import APIRouter, UploadFile
import shutil
from app.tasks.tasks import proccess_pic


router = APIRouter(
    prefix='/imges',
    tags=['Загрузка изображения'],
)


@router.post('/hotels')
async def add_hotel_image(name: int, file: UploadFile):
    file_path = f'app/static/images/{name}.webp'
    with open(file_path, 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)
    proccess_pic.delay(file_path)
            