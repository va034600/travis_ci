[![Build Status](https://travis-ci.org/va034600/travis_ci.svg?branch=master)](https://travis-ci.org/va034600/travis_ci)

# travis_ci

# setup
- pyenv
- pipenv

# list
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

# docker build
```
$ docker build -t va034600/sample_travis_ci:1 -f docker/Dockerfile .
```

# docker push
```
$ docker push va034600/sample_travis_ci:1
```

# docker-compose up
```
$ cd docker
$ cp .env.template .env
$ docker-compose up -d
```

```
$ docker login
```

- Using Docker Compose  
https://docs.travis-ci.com/user/docker/#using-docker-compose
- Build Stages: Sharing a Docker image  
https://docs.travis-ci.com/user/build-stages/share-docker-image/
