# API аналог ```booking.com``` 
### API аналог ```booking.com```, написанный на языке ```Python``` с помощью фреймворка ```FastAPI```, воспользоваться API можно после клонирования репозитория, добавления файла ```.env``` в корень репозитория с данными из файла ```env-example.txt``` и выполнения команды в режиме виртуального окружения ```uvicorn app.main:app --reload```. 
+ Документация API - ```127.0.0.1/docs```.

### Если Вы хотите развернуть данный проект с использованием ```Docker-compose```, создайте файл ```.env-no-dev``` в корне репозитория с данными из файла ```env-example.txt``` и находясь в репозитории сначало выполнить команду ```docker compose build```, а затем ```docker compose up```. 

+ Документация API - ```localhost:9000/docs```
+ БД - ```localhost:9001```
+ Flower - ```localhost:9002```
+ Grafana - ```localhost:3000```

### Стек технологий используемый в проекте: + Python, FastAPI + PostgreSQL, SQLAlchemy, Alembic, Redis + Celery, Flower + Авторизация по JWT-токену + Grafana, Prometheus + Docker, Docker-compose + Sentry
