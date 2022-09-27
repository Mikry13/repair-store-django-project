## Project structure

The main django app is called `app`. It contains `.env` file for django-environ. For examples see `src/app/.env.ci`. 

Also in the `app` are app-wide customizations like default models, admin classes etc. All the configurations are in `app/conf`

## Installing on a local machine
* The project requires `Python 3.10.7`

Install requirements:

```bash
$ pip install -r requirements.txt
```

Run the server:

```bash
$ cd src && cp app/.env.ci app/.env  # setup environment variables
$ docker-compose build
$ docker-compose up
```

#### Additions
You can also run django separately from database on your local machine 
if you build container with `postgres-docker-compose.yml` and set `.env > DATABASE_URL > "db"` to `localhost`

Then running will be like:
```bash
$ docker-compose -f postgres-docker-compose.yml
$ docker-compose build
$ docker-compose up
$ cd src && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver
```

### Note
* To run server on `Heroku`, set environment variable `HOST=HEROKU`.
* If you change environment variables, re-build container.
* _**Do not forget to specify default superuser in env**_

## Backend Code requirements

### Code Style
* KISS & DRY.
* Follow [Django Style Guide](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style).
* Follow [Django Best Practices](http://django-best-practices.readthedocs.io/en/latest/index.html).
* Use [Type Hints](https://www.python.org/dev/peps/pep-0484/)
* Use linters: [Flake8](https://pypi.python.org/pypi/flake8)
* **Move logic from views and serializers to services**
