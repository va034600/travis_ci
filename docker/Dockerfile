FROM python:3.6.10

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install pipenv

COPY ./Pipfile /usr/src/app/Pipfile
COPY ./Pipfile.lock /usr/src/app/Pipfile.lock

RUN pipenv install --system

COPY . /usr/src/app/

#CMD tail -f /dev/null

WORKDIR /usr/src/app/travis_ci
CMD python manage.py runserver 0.0.0.0:8000
