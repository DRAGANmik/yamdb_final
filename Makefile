grunserver:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

fixtures:
	python manage.py loaddata fixtures.json