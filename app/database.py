from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

from sqlalchemy import NullPool

if settings.MODE == 'TEST':
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {"poolclass": NullPool}

engine_nullpool = create_async_engine(DATABASE_URL,
                                      **DATABASE_PARAMS)

async_session_maker = sessionmaker(engine_nullpool,
                                   class_=AsyncSession,
                                   expire_on_commit=False)

class Base(DeclarativeBase):
    pass