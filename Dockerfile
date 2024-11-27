FROM ubuntu:latest
LABEL authors="nicho"

ENTRYPOINT ["top", "-b"]

#Dockerfile, Image, Container

FROM python:3.12

ADD A4.py .

CMD ["python", "./A4.py"]