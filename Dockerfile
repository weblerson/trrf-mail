FROM ubuntu:latest

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update

COPY downloads.sh .
RUN sh ./downloads.sh

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN apt-get install -y firefox
