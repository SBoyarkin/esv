#!/bin/bash
cd /var/www/site
python -m venv venv
echo 'Create venv'
source venv/bin/activate
pip install -r /var/www/site/requirements.txt
