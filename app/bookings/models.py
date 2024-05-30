from sqlalchemy import JSON, Column, Computed, Date, ForeignKey, Integer, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime

class Bookings(Base):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    date_from: Mapped[datetime]= mapped_column(Date, nullable=False)
    date_to: Mapped[datetime]= mapped_column(Date, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    total_cost: Mapped[int] = mapped_column(Computed('(date_to - date_from) * price'))
    total_days: Mapped[int] = mapped_column(Computed('date_to - date_from'))
    
    user: Mapped[list['Users']] = relationship(back_populates='booking')
    room: Mapped[list['Rooms']] = relationship(back_populates='booking')
    
    def __str__(self):
        return f'Booking #{self.id}'    