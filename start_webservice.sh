#!/bin/bash
# This script installs the right dependencies and starts the web service.
# The argument for this script are the following
#  - $1: either 'True' or 'False', depending whether you would like to install the Flask-MonitoringDashboard
#  - $2: either 'True' or 'False', depending whether you want to monitor outliers or not.
#  - $3: the outlier_detection_constant (must be an integer)
echo "1: $1"
echo "2: $2"

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

#configure dashboard
export DASHBOARD_CONFIG="./config.cfg"
echo "[dashboard]" >> ./config.cfg
echo "OUTLIERS_ENABLED=$2" >> ./config.cfg
echo "OUTLIER_DETECTION_CONSTANT=$3" >> ./config.cfg
cat ./config.cfg

pip3.6 install flask-cors --upgrade
cd zeeguu_api
sed -i "s/application.run(/application.run(debug=True,/g" __main__.py
cd ..
if [ "$1" == "False" ]; then
	pip uninstall Flask-MonitoringDashboard
	echo "Skipping Flask-MonitoringDashboard by removing every line that contains 'dashboard'"
	cd zeeguu_api	
	sed -i "/\b\(dashboard\)\b/d" app.py
	cat __main__.py
	cd ..
fi
python3.6 setup.py install
./run_tests.sh
./api_test.sh
