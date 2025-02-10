FROM python:3.10

WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["make", "run"]