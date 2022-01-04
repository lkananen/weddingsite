FROM python:3.9-alpine
LABEL maintainer="github.com/lkananen"

# Dependecies
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app
COPY ./entry.sh /entry.sh
RUN chmod +x /start.sh

#RUN useradd -m heroku
#USER heroku

CMD ["./entry.sh"]
