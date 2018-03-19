FROM ubuntu:17.10

WORKDIR /

COPY . .

RUN apt-get update
RUN apt-get install -y git wget python3.6 python3-venv

ARG dashboard
ENV dashboard=$dashboard

CMD ./deploy_app.sh $dashboard