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
(pd: I'm using AWS so I have to change de inbound rules of the instance to allow connections on 3306 port)

*change config file of mysql
in the file /etc/mysql/mysql.conf.d/mysqld.cnf change:
bind-address =  127.0.0.1
to 
bind-address =  0.0.0.0

then save and restart with
systemctl restart mysql.service

# Creation of tables
Next we create de DB named 'test_cuentaMovil' and tables used using Workbench

1 table named 'expense' with columns: id(int, autoincrement), description(varchar100), amount(float), date(datetime)

# To run the server gunicorn
* connect to the server using putty and private key
* go to directory of the flask server
* start venv with source venv/bin/activate
* create a file wsgi.py and import the main flask app and add it to main and run it
* start gunicorn with gunicorn --bind 0.0.0.0:5000 wsgi:app

# to stop gunicorn
command to see de PID of gunicorn process
* ps ax|grep gunicorn

command to kill the process
* kill -9 <PID_NUMBER>

# configuring gunicorn
Once we prove that our server work fine. We stop gunicorn.
And configure it as a service on ubuntu, that it will be waiting for a request in a socket.

# Make a curl post from windows
curl -i -X POST -H "Content-Type:application/json" -d "{""description"": ""Frodo"",  ""amount"" : 10 }" http://x.x.x.x/addexpense

# Changing database
it's create a new database with the new table User and join it to the table Expense. Add foreign key to Expense table to create a 1 to M relationship.

Then its change the file DBConnection, the create engine part to point to the new DB(from test_cuentaMovil --> to --> test_cuentaMovilv2). And test if can save expense data in the new database.
