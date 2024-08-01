FROM python:3.9-slim-buster

RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf

WORKDIR /myportfolio

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
