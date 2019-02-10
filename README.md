# cuentaMovilServer
The backend side of the cuentaMovil app

# instalation of Nginx
First, it was installed Nginx on Ubuntu server 18.

Nginx Instalation
$sudo apt update
$sudo apt install nginx

We will not activate the firewall because we going to connect using other ports in the future.

To see Nginx status:
$systemctl status nginx

It will show an error:
nginx.service: Failed to read PID from file /run/nginx.pid: Invalid argument

It fix with:
$mkdir /etc/systemd/system/nginx.service.d
$sudo printf "[Service]\nExecStartPost=/bin/sleep 0.1\n" | sudo tee /etc/systemd/system/nginx.service.d/override.conf
$systemctl daemon-reload
$systemctl restart nginx

To verify run again the next command:
$systemctl status nginx

# Instalation of python dependencies
For mysql conector
Error: 
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-8pl0ztdz/mysqlclient/
Solution:
Out of the venv execute:
sudo apt install libmysqlclient-dev
Inside the venv(python 3.6) execute:
pip install mysqlclient

# Instalation of MYSQL
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
*put a password to root user
connect with:
mysql -u root -p

*inside mysql
CREATE USER 'alex'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'%' WITH GRANT OPTION;
* % for remote conections

*change config file of mysql
in the file /etc/mysql/mysql.conf.d/mysqld.cnf change:
bind-address =  127.0.0.1
to 
bind-address =  0.0.0.0

then save and restart with
systemctl restart mysql.service

