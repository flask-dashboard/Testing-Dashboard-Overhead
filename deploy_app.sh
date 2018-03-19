#!/bin/bash
# This script installs the right dependencies and starts the web service.

git clone https://github.com/zeeguu-ecosystem/Zeeguu-Core
cd Zeeguu-Core

# Hack to remove the word 'sudo' from the install-script
sed 's/sudo//g' ubuntu_install.sh > ubuntu_install2.sh
chmod 777 ubuntu_install2.sh

# Execute the install script
./ubuntu_install2.sh
