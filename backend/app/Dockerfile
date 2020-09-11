FROM python:3.6-alpine3.10

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt 
RUN apk update
RUN apk add vim

COPY . /app

EXPOSE 5001

CMD python apirestful.py