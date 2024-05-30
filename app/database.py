from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

from sqlalchemy import NullPool

DATABASE_PARAMS = {"poolclass": NullPool}

engine_nullpool = create_async_engine(settings.DATABASE_URL,
                                        **DATABASE_PARAMS)

async_session_maker = sessionmaker(engine_nullpool,
                                   class_=AsyncSession,
                                   expire_on_commit=False)

class Base(DeclarativeBase):
    pass