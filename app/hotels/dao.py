from sqlalchemy import text
from datetime import date

from app.dao.base import BaseDAO
from app.hotels.models import Hotels, Rooms
from app.bookings.models import Bookings
from app.database import async_session_maker


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_all_by_location_with_rooms_left(cls, 
                                                   location: str, 
                                                   date_from: date, 
                                                   date_to: date):
        async with async_session_maker() as session:
           
            query = f'''
            with rooms_left as (select rooms.hotel_id, count(bookings.id) as rooms_bron
            from bookings, rooms
            where bookings.room_id = rooms.id and 
            ((bookings.date_from>='{date_from}' and bookings.date_from<'{date_to}')
            or (bookings.date_from<='{date_from}' and bookings.date_to>='{date_from}')
            or (bookings.date_to>'{date_from}' and bookings.date_to<='{date_from}'))
            and rooms.hotel_id in (select id from hotels where location like '%{location}%')
            group by rooms.hotel_id
            )
            select hotels.id, hotels.name, hotels.location,
                    hotels.services, hotels.rooms_quality, hotels.image_id,
                    (hotels.rooms_quality - coalesce  (rooms_left.rooms_bron, 0)) as rooms_left		
            from hotels
            left outer join rooms_left
            on hotels.id = rooms_left.hotel_id
            where hotels.location like '%{location}%'
            '''
           
            # query = select(Hotels.id, Hotels.name, Hotels.location,
            #                Hotels.services, Hotels.rooms_quality, Hotels.image_id,
            #                (Hotels.rooms_quality - (
            #                    select(func.count(Bookings.id)).where(
            #                        and_(Bookings.room_id == Rooms.id,
            #                             or_(
            #                                 and_(
            #                                     Bookings.date_from>='2023-06-10',
            #                                     Bookings.date_from<'2023-06-20', 
            #                                     ),
            #                                 and_(
            #                                     Bookings.date_from<='2023-06-10',
            #                                     Bookings.date_to>='2023-06-20', 
            #                                     ),
            #                                 and_(
            #                                     Bookings.date_to>'2023-06-10',
            #                                     Bookings.date_to<='2023-06-20', 
            #                                     ),             
            #                                 ),
            #                             Rooms.hotel_id.in_(
            #                                                 select(Hotels.id).where(
            #                                                                         Hotels.location.like('Республика Алтай%')
            #                                                                         )
            #                                               )
            #                             )                                   
            #                                                         )
            #                                         )
                                                    
            #                 ).label('rooms_left')
            #               ).where(
            #                         and_(
            #                             Bookings.room_id == Rooms.id,
            #                             Rooms.hotel_id == Hotels.id,
            #                             Hotels.location.like('Республика Алтай%')
            #                             )
            #                      ).group_by(
            #                                 Hotels.id
            #                                 )
            result = await session.execute(text(query))
            return result.mappings().all()

    @classmethod
    async def find_all_rooms_in_hotel_by_id(cls,
                                            id: int,
                                            date_from: date,
                                            date_to: date):
        async with async_session_maker() as session:
            query = f'''
            with rooms_left as (select rooms.id, count(bookings.id) as rooms_bron
            from bookings, rooms
            where bookings.room_id = rooms.id and 
            ((bookings.date_from>='{date_from}' and bookings.date_from<'{date_to}')
            or (bookings.date_from<='{date_from}' and bookings.date_to>='{date_to}')
            or (bookings.date_to>'{date_from}' and bookings.date_to<='{date_to}'))
            and rooms.hotel_id = {id}
            group by rooms.id
            )
            select rooms.id, rooms.hotel_id, rooms.name,
                    rooms.description, rooms.price, rooms.services,
                    (rooms.quality - coalesce  (rooms_left.rooms_bron, 0)) as rooms_left,
                    ((cast('{date_to}' as date) - cast('{date_from}' as date)) * price) as total_cost,
                    rooms.image_id 
            from rooms
            left outer join rooms_left
            on rooms.id = rooms_left.id
            where rooms.hotel_id = {id}
            '''
            result = await session.execute(text(query))
            return result.mappings().all()