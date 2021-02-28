# ds18b20-ws
ds18b20 web service

```
apt-get update
apt-get install -y python3-pip python3-dev python3-psycopg2 supervisor 
rehash
pip3 install -r requirements.txt
python3 app.py
```

install as a service:

```
cp ds18b20-ws.conf /etc/supervisor/conf.d
rehash
supervisorctl reload
supervisorctl status
```
