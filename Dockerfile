FROM python:3.10-slim

RUN apt-get update && apt-get install -y git

COPY requirements.txt /requirements.txt

WORKDIR /PiroAutoFilterBot

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

COPY . .

CMD ["python", "bot.py"]
