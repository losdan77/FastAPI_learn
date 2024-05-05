from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'postgres'
DB_PASS = '50047648'
DB_NAME = 'postgres'

DATADASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATADASE_URL)

async_session_maker = sessionmaker(engine,
                                   calss_=AsyncSession,
                                   expire_on_commit=False)

class Base(DeclarativeBase):
    pass