#!/bin/bash
cd /var/www/esv
python -m venv venv
echo 'Create venv'
source venv/bin/activate
pip install -r /var/www/esv/backend/requirements.txt
