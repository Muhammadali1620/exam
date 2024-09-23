FROM python:3.12.3-slim

WORKDIR /app

COPY requirements.txt .

COPY .env .

RUN pip install -r requirements.txt

COPY ./src /app