## Project Info

## Requirements to run
* Recommend creating a local virtual environment.
* If you use asdf as a language manager, you can `asdf install` which should grab the python version specified in the `.tool-versions`
1.  `pip install -r ./requirements.txt`
2.  Set the environment variable `DJANGO_SECRET_KEY`
3.  Run `python manage.py migrate --run-syncdb` to setup a local sqlite database.
4.  Run `python manage.py seed_data_records` to populate the database.
5.  Run `python manage.py runserver_plus`
6.  Navigate to `http://127.0.0.1:8000/fool/home`
