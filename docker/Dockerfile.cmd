FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y iputils-ping

CMD ["ping", "-c", "4", "google.com"]