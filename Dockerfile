FROM alpine:latest
RUN apk add python3 && apk add py-pip
COPY requirements.txt /tmp
RUN pip install -r requirements.txt && rm -rf /tmp
COPY docker_lite.py .
