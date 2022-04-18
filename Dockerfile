FROM python:bullseye

EXPOSE 5000

COPY . /app

RUN pip3 install -r /app/requirements.txt

ENV FLASK_APP="/app/bankingapp/__init__.py"

ENV LC_ALL=C.UTF-8

ENV LANG=C.UTF-8

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

