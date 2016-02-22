After initial configuration of raspberry pi run the following commands in terminal. 

sudo apt-get update
sudo apt-get upgrade
sudo apt-get installpython-serial apache2 libapache2-mod-wsgi python-setuptools python-flask


then edit your virtual host in /etc/apache2/sites-enabled
 visit http://pastebin.com/raw/vLkikT2m to find the edits , make only additions and do  not overwrite.

Edit  /etc/apache/envvars file using following command

sudo nano /etc/apache/envvars

make the following changes in code snippet.

export APACHE_RUN_USER=pi
export APACHE_RUN_GROUP=pi

run the following commands.

a2enmod wsgi

/etc/init.d/apache2 restart
