## Simple Python HTTPS

This is simple https code that learning from https://realpython.com/python-https/

----

### Install Dependencies
1. Make sure you have libssl-dev before.
2. run ```pip install -r requirements.txt``` to install all dependencies

### How to run
#### server side
1. generate self signed certificate.
2. run ```uwsgi --master --https localhost:1234,server-public-key.pem,server-private-key.pem --mount /=server:app```
3. enter passphrase.
#### server side
1. run python script ```./client.py```