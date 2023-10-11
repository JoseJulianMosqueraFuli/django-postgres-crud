FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install -r requirements.txt 'Python -m permit specify the same pip installes is excecuted in my docker'

COPY . /code/
