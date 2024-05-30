from sqlalchemy import JSON, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Hotels(Base):
    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON, nullable=True)
    rooms_quality: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int] = mapped_column(nullable=True)

    room = relationship('Rooms',
                        back_populates='hotel')
    
    def __str__(self):
        return f'{self.name}'

class Rooms(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'),
                                          nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON, nullable=True)
    quality: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]  = mapped_column(nullable=True)

    booking: Mapped[list['Bookings']] =  relationship(back_populates='room')
    hotel: Mapped[list['Hotels']] = relationship(back_populates='room')
    
    def __str__(self):
        return f'{self.name}'