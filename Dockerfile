# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get -y install gcc
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP=application.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]