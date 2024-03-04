createsuperuser:
	python manage.py createsuperuser

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

sass:
	sass --watch ./scss/style.scss ./static/css/style.css