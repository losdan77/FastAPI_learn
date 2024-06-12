FROM python:3.10

RUN mkdir /booking_app

WORKDIR /booking_app

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY . .

RUN chmod a+x /booking_app/docker/*.sh

#для деплоя на хостинге
RUN alembic upgrade head

CMD [ "gunicorn", "app.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000" ]

