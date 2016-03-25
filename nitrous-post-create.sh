#!/bin/bash
cd ~/code
virtualenv -p python3 average_alpr
cd ~/code/average_alpr
source bin/activate
pip install tornado flask requests urllib3
cat create.sql | sqlite3 average_check.db
