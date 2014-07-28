jinja flask python for bitcoin rpc
=========

Demo bitcoin walled for the cloud.

  - Responsive mobile 
  - RPC Bitcoin
  - Cloud wallet bitcoin

> Send payments to another address bitcoin with python
 


Installation Centos 6
--------------

```sh
yum install python 
yum install python-setuptools
easy_install pip
pip install virtualenv 
pip install Flask 
pip install flask_bootstrap
pip install flask_wtf
pip install python-bitcoinrpc
yum install -y mod_wsgi  
vi /etc/httpd/conf.d/wsgi.conf 
/etc/init.d/httpd restart 
chcon -R -t httpd_config_t /home/websites/paymentbitcoin/ 
```

##### Configure your httpd apache web server

```sh
Alias /paybitSource /home/websites/paymentbitcoin/app/wallet.py
WSGIDaemonProcess wallet user=apache group=apache threads=5
WSGIScriptAlias /paybit /home/websites/paymentbitcoin/app/wrapper.wsgi
WSGIScriptReloading On
<Directory /home/websites/paymentbitcoin/app/>
        Allow from all
</Directory>

```

##### Configure your bitcoin daemon/server

```sh
Vi /home/bit92347**/bitcoin.conf
server=1
daemon=1
rpcuser=whatever
rpcpassword=whatever
#rpcallowip=*.*.*.*
rpcport=7244
port=7245
#rpcallowip=1-.... 
```

www.jamesjara.com