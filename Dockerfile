FROM python:3

WORKDIR /usr/src/app

RUN pip install flask_monitoringdashboard

COPY . .

ARG dashboard
ENV dashboard=$dashboard

CMD python ./main.py $dashboard