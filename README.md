# travis_ci

# setup
- pyenv
- pipenv

```
$ pipenv --python 3.6
$ pipenv install django==2.2.3
$ pipenv shell
(travis_ci) $ django-admin startproject travis_ci
(travis_ci) $ cd travis_ci
(travis_ci) $ python manage.py migrate
(travis_ci) $ python manage.py runserver
```

```
$ cd docker
$ docker-compose up
```

```
http://127.0.0.1:8000/
```

```
$ docker build -t sample/sample_travis_ci:1 -f docker/Dockerfile .
```