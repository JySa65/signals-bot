FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app/
