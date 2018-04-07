#!/bin/bash
# Use this script for starting everything

echo "Stop and remove running containers"
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# When running in parallel, make sure that PORT_A, PORT_B and PORT_C are all unique
PORT_A=9001
PORT_B=9002
PORT_C=9003

# Build the webservice
docker build -t webservice .

# Deploy webservice with the Dashboard
echo "Deploy the three webservices all at once"
docker run -d --name with_dashboard_and_outliers -p PORT_A:9001 \
	-e dashboard=True \
	-e with_outliers=True \
	-e outlier="0" webservice
docker run -d --name with_dashboard_but_no_outliers -p PORT_B:9001 \
	-e dashboard=True \
	-e with_outliers=False \
	-e outlier="10000" webservice
docker run -d --name without_dashboard -p PORT_C:9001 \
	-e dashboard=False \
	-e with_outliers=False \
	-e outlier="2.5" webservice

python -m testing http://localhost:PORT_A/ with_dashboard_and_outliers \
				  http://localhost:PORT_B/ with_dashboard_but_no_outliers \
				  http://localhost:PORT_C/ without_dashboard

# Stop previous container
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)