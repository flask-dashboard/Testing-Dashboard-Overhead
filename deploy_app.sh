#!/bin/bash
# This script installs the right dependencies and starts the web service.



# MSQL Settings
debconf-set-selections <<< 'mysql-server-5.7 mysql-server/root_password password password'
debconf-set-selections <<< 'mysql-server-5.7 mysql-server/root_password_again password password'
service mysql start
mysql -e "create database IF NOT EXISTS zeeguu_test; grant all on zeeguu_test.* to 'zeeguu_test'@'localhost' identified by 'zeeguu_test';" -uroot


# VIRTUALENV SETTINGS
VIRTENVDIR=~/.venvs
ZENV=z_env

mkdir $VIRTENVDIR
python3.6 -m venv $VIRTENVDIR/$ZENV
source $VIRTENVDIR/$ZENV/bin/activate



# Install Zeeguu-Core
git clone https://github.com/zeeguu-ecosystem/Zeeguu-Core
cd Zeeguu-Core
pip3.6 install wheel
pip3.6 install -r requirements.txt
python3.6 setup.py develop
./run_tests.sh
# Populate the webservice
python3.6 -m zeeguu.populate
cd ..




# Install Python-Translators
git clone https://github.com/zeeguu-ecosystem/Python-Translators
cd Python-Translators
pip install -r requirements.txt
python3.6 setup.py install
cd ..



# Install Zeeguu-API
git clone https://github.com/zeeguu-ecosystem/Zeeguu-API
cd Zeeguu-API
pip3.6 install flask-cors --upgrade
if [ "$1" == "True" ]; then
	echo "Installing Flask-MonitoringDashboard"
	pip3.6 install flask_monitoringdashboard
else
	echo "Skipping Flask-MonitoringDashboard"
fi
pip3.6 list
python3.6 setup.py develop
./run_tests.sh
./api_test.sh