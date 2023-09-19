FROM python:3.8-slim-buster

ARG HELLO_STR=""
ARG MAINTAINER="noname"

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt update && apt install -y vim

COPY . .

EXPOSE 5000

ENV HELLO_STRING="${HELLO_STRING}"

LABEL org.opencontainers.image.authors="${MAINTAINER}"

CMD [ "python3", "app.py"]