from email.message import EmailMessage
from pydantic import EmailStr

from app.config import settings


def create_booking_confirm_template(booking: dict,
                                    email_to: EmailStr,):
    email = EmailMessage()

    email['Subject'] = 'Confirm booking'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f'''
            <h1>TY for booking</h1>
            Your booking from {booking['date_from']} to {booking['date_to']}
        ''',
        subtype='html'
    )
    return email


def create_booking_notice_template(booking: dict,
                                     email_to: EmailStr):
    email = EmailMessage()

    email['Subject'] = 'Notice booking'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f'''
            <h1> Hello, notice for your booking</h1> 
            In {booking['name']}
            from {booking['date_from']} to {booking['date_to']}
        ''',
        subtype='html' 
    )
    return email 