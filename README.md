# cuentaMovilServer
The backend side of the cuentaMovil app

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
