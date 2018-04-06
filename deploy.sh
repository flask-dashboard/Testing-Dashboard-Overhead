#!/bin/bash
# Use this script for starting everything

echo "Stop and remove running containers"
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Build the webservice
# docker build -t webservice .

# Deploy webservice with the Dashboard
echo "Deploy the three webservices all at once"
docker run -d --name with_dashboard_and_outliers -p 9001:9001 \
	-e dashboard=True \
	-e outlier="0" webservice
docker run -d --name with_dashboard_but_no_outliers -p 9002:9001 \
	-e dashboard=True \
	-e outlier="10000" webservice
docker run -d --name without_dashboard -p 9003:9001 \
	-e dashboard=False \
	-e outlier="2.5" webservice

python -m testing http://localhost:9001/ with_dashboard_and_outliers \
				  http://localhost:9002/ with_dashboard_but_no_outliers \
				  http://localhost:9003/ without_dashboard

# Stop previous container
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)