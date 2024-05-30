from sqlalchemy import JSON, Column, Computed, Date, ForeignKey, Integer, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=True)

    booking: Mapped[list['Bookings']] = relationship(back_populates='user')
    
    
    def __str__(self):
        return f'{self.email}'