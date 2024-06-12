from app.database import async_session_maker

from sqlalchemy import select, insert, delete, text

class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()
        
    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()
        
    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
        
    @classmethod
    async def delete(cls, id: int, user_id: int):
        async with async_session_maker() as session:
            query_select = select(cls.model).filter_by(id = id, user_id = user_id)
            result = await session.execute(query_select)
            if result.scalar():
                query_delete = delete(cls.model).where(cls.model.id == id, 
                                                       cls.model.user_id == user_id)
                delete_result = await session.execute(query_delete)
                await session.commit()
                return 'successful'
            else:
                return None
            
    @classmethod
    async def import_fom_csv(cls, table_name: str):
        async with async_session_maker() as session:
            query_import = f"COPY {table_name} FROM '/home/booking_app/app/csv/file.csv' DELIMITER ',' CSV HEADER"
            await session.execute(text(query_import))
            await session.commit()
            return 'successful'