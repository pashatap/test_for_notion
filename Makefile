run:
	python manage.py runserver
migrate:
		python manage.py makemigrations
		python manage.py migrate
createsuperuser:
		python manage.py createsuperuser

write_in_db:
		python manage.py write_in_db