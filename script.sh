pip install -r requirements.txt
curl https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -o cloud_sql_proxy
chmod +x cloud_sql_proxy
./cloud_sql_proxy -instances=sql-instance-4=tcp:3306
python connect.py