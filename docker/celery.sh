#!/bin/bash

celery --app=app.tasks.celery_app:celery worker -l INFO