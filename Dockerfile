FROM python:3.9

WORKDIR /app

RUN pip install --upgrade setuptools

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

# need better implementation #
COPY ./secrets /app/secrets 

COPY ./run.sh /app/run.sh

RUN chmod +x /app/run.sh

COPY .env /app/.env

COPY ./src /app/src

CMD ["sh", "./run.sh"]