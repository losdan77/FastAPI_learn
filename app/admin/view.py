from sqladmin import ModelView
from app.users.models import Users
from app.bookings.models import Bookings
from app.hotels.models import Hotels, Rooms


class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email, Users.role]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = 'Пользователь'
    name_plural = 'Пользователи'
    icon = 'fa-solid fa-user'


class BookingAdmin(ModelView, model=Bookings):
    column_list = '__all__'
    name = 'Бронирование'
    name_plural = 'Бронирования'
    icon = 'fa-solid fa-book'


class HotelsAdmin(ModelView, model=Hotels):
    column_list = '__all__'
    name = 'Отель'
    name_plural = 'Отели'
    icon = 'fa-solid fa-hotel'    


class RoomsAdmin(ModelView, model=Rooms):
    column_list = '__all__'
    name = 'Номер'
    name_plural = 'Номера'
    icon = 'fa-solid fa-hotel'