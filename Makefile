install:
	poetry install

dev:
	python manage.py runserver

start:
	gunicorn task_manager.wsgi