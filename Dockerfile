FROM ubuntu:16.04

MAINTAINER Chris Kretler <ckretler@umich.edu>

RUN apt-get update \
	&& apt-get install -y python python-pip \
	&& pip install requests

WORKDIR /app/

COPY . /app/

CMD ["python", "computive.py"]
