FROM python:3.9.9-slim-buster
LABEL maintainer="lkananen"

RUN apt-get update && apt-get install -y python3-dev build-essential

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "source.main:app"]
