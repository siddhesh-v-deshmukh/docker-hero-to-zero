FROM centos:latest

WORKDIR /app

COPY . /app

RUN yum update
RUN yum install -y python3

CMD ["python3","app.py"]

