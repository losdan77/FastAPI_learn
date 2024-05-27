from sqlalchemy import select, func, and_, or_, insert, text
from datetime import date

from app.dao.base import BaseDAO
from app.bookings.models import Bookings
from app.hotels.models import Rooms, Hotels
from app.database import async_session_maker


class BookingsDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls,
            user_id: int,
            room_id: int,
            date_from: date,
            date_to: date
        ):
        
        '''
        with booked_rooms as (
        select * from bookings
        where room_id = 1 and 
        (date_from>='2023-06-10' and date_from<='2023-06-20') or 
        (date_from<='2023-06-10' and date_to>'2023-06-10')
        )
        select (rooms.quality -count(booked_rooms.room_id)) from rooms
        left join booked_rooms on booked_rooms.room_id = rooms.id
        where rooms.id = 1
        group by rooms.quality, booked_rooms.room_id         
        '''
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id==room_id,
                    or_(
                        and_(
                            Bookings.date_from>=date_from,
                            Bookings.date_from<date_to, 
                            ),
                        and_(
                            Bookings.date_from<=date_from,
                            Bookings.date_to>=date_to, 
                            ),
                        and_(
                            Bookings.date_to>date_from,
                            Bookings.date_to<=date_to, 
                            ),             
                        ),
                    ),
            ).cte('booked_rooms')

            '''
            select (rooms.quality -count(booked_rooms.room_id)) from rooms
            left join booked_rooms on booked_rooms.room_id = rooms.id
            where rooms.id = 1
            group by rooms.quality, booked_rooms.room_id  
            '''
            get_rooms_left = select(
                (Rooms.quality - func.count(booked_rooms.c.room_id)).label('rooms_left')
            ).select_from(Rooms).outerjoin(
                booked_rooms, booked_rooms.c.room_id == Rooms.id
            ).where(Rooms.id == room_id).group_by(
                Rooms.quality, booked_rooms.c.room_id
            )

            rooms_left = await session.execute(get_rooms_left)
            rooms_left: int = rooms_left.scalar()

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()

                add_booking = insert(Bookings).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price,
                ).returning(Bookings)
                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
            else:
                return None    
            
    
    @classmethod
    async def check_bookings(cls,
                             date_from: date):
        async with async_session_maker() as session:
            query = f'''select users.email, bookings.date_from,
                            bookings.date_to, hotels."name"  
                        from bookings, users, hotels, rooms
                        where bookings.user_id = users.id and
                            hotels.id = rooms.hotel_id and
                            bookings.room_id = rooms.id and
                            bookings.date_from = '{date_from}'
                    '''

            result = await session.execute(text(query))
            return result.mappings().all()