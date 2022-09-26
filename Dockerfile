FROM python:3.9.9-slim-buster
ENV PYTHONBUFFERED=1
WORKDIR /django
COPY requirements.in requirements.in
RUN pip install -r requirements.in