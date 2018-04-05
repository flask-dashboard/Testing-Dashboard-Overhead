#!/bin/bash
# Use this script for starting everything

echo "Stop and remove running containers"
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Build the webservice
docker build -t webservice .

# Deploy webservice with the Dashboard
echo "Deploy the webservice with the dashboard (and outliers)"
docker run -d --name with_dashboard_and_outliers -p 9001:9001 \
	-e dashboard=True \
	-e outlier="0" webservice
python -m testing http://localhost:9001/ with_dashboard_and_outliers

Stop previous container
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Deploy webservice with the Dashboard
echo "Deploy the webservice with the dashboard (but without outliers)"
docker run -d --name with_dashboard_but_no_outliers -p 9001:9001 \
	-e dashboard=True \
	-e outlier="10000" webservice
python -m testing http://localhost:9001/ with_dashboard_but_no_outliers

# Stop previous containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Deploy webservice without the Dashboard
echo "Deploy the webservice without the dashboard"
docker run -d --name without_dashboard -p 9001:9001 \
	-e dashboard=False \
	-e outlier="2.5" webservice
python -m testing http://localhost:9001/ without_dashboard

# Stop all containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
