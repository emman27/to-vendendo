FROM python:slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update && apt install -y build-essential

ADD ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app

ENV FLASK_APP tovendendo/__init__.py 

EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0"]
