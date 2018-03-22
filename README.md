# Dashboard-overhead
This is a repository for investigating the overhead of the [Flask-MonitoringDashboard](https://github.com/flask-dashboard/Flask-MonitoringDashboard).

## How to install?
Make sure that you've installed [docker](https://docs.docker.com/install/).
Furthermore, install the right Python packages using:
```
pip install -r requirements.txt
``` 


## How to run?
Run the following command for executing the script:
```
./deploy.sh
```
  
## How does it work?
The Flask application is deployed within a [Docker-image](https://hub.docker.com/_/python/).

This tries to produce two equivalent execution environments. In one environment the Dashboard is included, in the other it is not.

The difference in results is assumed to be due to the Dashboard.

