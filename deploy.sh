#!/bin/bash
# Use this script for starting everything

echo "Stop and remove running containers"
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

if ! [ -z ${GOOGLE_TRANSLATE_API_KEY} ] || ! [ -z ${MICROSOFT_TRANSLATE_API_KEY} ] ; then
	echo "GOOGLE_TRANSLATE_API_KEY and MICROSOFT_TRANSLATE_API_KEY must be set in order to run this script."
	exit 1
fi


# Build the webservice
docker build -t webservice .

# Deploy webservice with the Dashboard
echo "Deploy the webservice with the dashboard"
docker run -d --name with_dashboard -p 9001:9001 -e dashboard=True -e google="$GOOGLE_TRANSLATE_API_KEY" -e microsoft="$MICROSOFT_TRANSLATE_API_KEY" webservice
python -m testing http://localhost:9001/ with_dashboard

Stop previous container
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Deploy webservice without the Dashboard
echo "Deploy the webservice without the dashboard"
docker run -d --name without_dashboard -p 9001:9001 -e dashboard=False -e google="$GOOGLE_TRANSLATE_API_KEY" -e microsoft="$MICROSOFT_TRANSLATE_API_KEY" webservice
python -m testing http://localhost:9001/ without_dashboard

# Stop all containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
