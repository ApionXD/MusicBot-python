# syntax=docker/dockerfile:1
FROM alpine:3.15.4
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apk add --no-cache python3-dev ffmpeg gcc musl-dev libffi-dev
RUN python3 -m ensurepip && pip3 install -r requirements.txt
RUN apk del gcc
copy src/ .
CMD [ "python3", "main.py"]