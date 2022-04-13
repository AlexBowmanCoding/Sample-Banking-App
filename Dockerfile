FROM ubuntu:18.04 as base

COPY . /app

RUN apt update -y && apt install -y python3 python3-pip libpq-dev

FROM base as app

RUN pip3 install -r /app/requirements.txt

ENV FLASK_APP="/app/src/__init__.py"

ENV LC_ALL=C.UTF-8

ENV LANG=C.UTF-8

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

