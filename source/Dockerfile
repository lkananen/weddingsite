FROM python:3.9-slim
LABEL maintainer="github.com/lkananen"

# Dependecies
RUN apt-get update && apt-get install -y python3-dev build-essential

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app
COPY ./entry.sh /entry.sh
RUN chmod +x /start.sh

#RUN useradd -m heroku
#USER heroku

CMD ["./entry.sh"]
