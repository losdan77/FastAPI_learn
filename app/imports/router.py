import csv
from fastapi import APIRouter, UploadFile, File

from app.dao.base import BaseDAO

router = APIRouter(
    prefix='/import',
    tags=['Импорт из CSV'],
)


@router.post('/{table_name}')
async def import_data_from_csv(table_name: str, file: UploadFile):
    #result_import = await BaseDAO.import_fom_csv(table_name, file)
    #return result_import
    if file.content_type == 'text/csv':
        file_csv = await file.read()
        with open ('app/csv/file.csv', 'wb') as f:
            f.write(file_csv)
        return {'filename': file.filename}
    else:
        return 'Неверный формат файла'