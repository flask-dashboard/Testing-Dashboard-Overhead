#!/bin/bash

NUM_REQUESTS=100

echo "Stop and remove running containers"
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Build the webservice
docker build -t webservice .

echo "Deploy the webservice with the dashboard"
docker run -it -d --name app_with_dashboard -p 5000:5000 -e dashboard=True webservice
echo "Wait until the webservice is successfully started"
sleep 5
python test.py $NUM_REQUESTS


docker stop $(docker ps -aq)
echo "Deploy the webservice without the dashboard"
docker run -it -d --name app_without_dashboard -p 5000:5000 -e dashboard=False webservice
echo "Wait until the webservice is successfully started"
sleep 5
python test.py $NUM_REQUESTS
