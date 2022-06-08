#! /bin/bash

pip3 install -r requirements.txt;
curl https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -o cloud_sql_proxy;
chmod +x cloud_sql_proxy;
./cloud_sql_proxy -instances=theloonesql-instance-6=tcp:3306 &
python3 connect.py;
