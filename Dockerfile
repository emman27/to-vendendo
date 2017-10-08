FROM python:slim

LABEL maintainer="emmanuel.goh.7@gmail.com" 

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update && apt install -y build-essential

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP tovendendo/__init__.py 

EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0"]
