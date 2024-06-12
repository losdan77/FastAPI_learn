import csv
from fastapi import APIRouter, UploadFile, File

from app.dao.base import BaseDAO

router = APIRouter(
    prefix='/import',
    tags=['Импорт из CSV'],
)


@router.post('/{table_name}')
async def import_data_from_csv(table_name: str, file: UploadFile):
    if file.content_type == 'text/csv':
        file_csv = await file.read()
        with open ('app/csv/file.csv', 'wb') as f:
            f.write(file_csv)
        result_import = await BaseDAO.import_fom_csv(table_name)
        return result_import
    else:
        return 'Неверный формат файла'