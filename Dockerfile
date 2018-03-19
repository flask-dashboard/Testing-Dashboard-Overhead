FROM ubuntu:17.10

WORKDIR /

COPY . .

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y git wget python3-venv python3.6-dev


ARG dashboard
ENV dashboard=$dashboard

CMD ./deploy_app.sh $dashboard