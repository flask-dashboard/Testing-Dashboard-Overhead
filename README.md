# Dashboard-overhead
This is a repository for investigating the overhead of the [Flask-MonitoringDashboard](https://github.com/flask-dashboard/Flask-MonitoringDashboard).

## How to run?
Run the following command for executing the script:
```
./deploy.sh
```
Make sure that you've met the following requirements:
- make 'deploy.sh' executable ($ chmod 777 deploy.sh)
- install package 'requests' for python3 ($ pip3 install requests)

## How does it work?
The Flask application is deployed within a [Docker-image](https://hub.docker.com/_/python/).

This tries to produce two equivalent execution environments. In one environment the Dashboard is included, in the other it is not.

The difference in results is assumed to be due to the Dashboard.

## What is left ToDo:
1. Enable monitoring of endpoints in Dashboard (Automatically)
2. Determine which (and how often) endpoints are tested?
3. Automatically compare the results of both output-files