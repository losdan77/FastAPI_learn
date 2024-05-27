 #celery --app=app.tasks.celery_app:celery worker -l INFO -B
from app.tasks.celery_app import celery
import smtplib
from app.tasks.email_templates import create_booking_notice_template
from app.config import settings

from datetime import datetime, date, timedelta
from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking

from asgiref.sync import async_to_sync


async def check_booking_tomorrow():
    tomorrow_date = (datetime.now() + timedelta(days=1)).date()
    return await BookingsDAO.check_bookings(tomorrow_date)


async def check_booking_tree_days():
    tree_plus_date = (datetime.now() + timedelta(days=3)).date()
    return await BookingsDAO.check_bookings(tree_plus_date)


@celery.task(name='booking_for_tomorrow')
def booking_for_tomorrow():

    print(datetime.now().date())
    tomorrow_booking = async_to_sync(check_booking_tomorrow)()
    if not tomorrow_booking:
        return None
    print(tomorrow_booking)

    for booking in tomorrow_booking:
        email_to_mock = settings.SMTP_USER #здесь должно быть booking['email']
        msg_content = create_booking_notice_template(booking,
                                                     email_to_mock) #Отправляю самому себе
        
        with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.login(settings.SMTP_USER, settings.SMTP_PASS)
            server.send_message(msg_content) 


@celery.task(name='booking_for_3_days')
def booking_for_3_days():

    print(datetime.now().date())
    tree_days_booking = async_to_sync(check_booking_tree_days)()
    if not tree_days_booking:
        return None
    print(tree_days_booking)

    for booking in tree_days_booking:
        email_to_mock = settings.SMTP_USER #здесь должно быть booking['email']
        msg_content = create_booking_notice_template(booking,
                                                     email_to_mock) #Отправляю самому себе
        
        with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.login(settings.SMTP_USER, settings.SMTP_PASS)
            server.send_message(msg_content)

    
    