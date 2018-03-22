FROM ubuntu:17.10

WORKDIR /

COPY . .

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y git wget python3-venv python3.6-dev build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libmysqlclient-dev mysql-client-core-5.7 mysql-server libmysqlclient-dev python-mysqldb

ARG dashboard
ENV dashboard=$dashboard

CMD ./start_webservice.sh $dashboard