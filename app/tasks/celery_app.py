from celery import Celery
from celery.schedules import crontab


celery = Celery(
    'tasks',
    broker='redis://localhost:6379',
    include=['app.tasks.tasks',
             'app.tasks.scheduled'],
)


celery.conf.beat_schedule = {
    'Booking_for_tomorrow': {
        'task': 'booking_for_tomorrow',
        'schedule': 20, #seconds
        #'schedule': crontab(minute='10', hour='9'), #по нулевому меридиану время
    },
    'Booking_for_3_days': {
        'task': 'booking_for_3_days',
        'schedule': 20, #seconds
        #'schedule': crontab(minute='30', hour='15'), #по нулевому меридиану время
    }
}