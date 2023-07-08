#!/usr/bin/env bash
# Script sets up a web server for the deployment of 'web_static'

sudo apt-get -y update && sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/releases/test/ \
	&& touch /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared/

printf "<html>\n\
\t<head>\n\
\t\t<body>\n\
\t\t\tHolberton School\n\
\t\t</body>\n\
\t</head>\n\
</html>" > /data/web_static/releases/test/index.html

# Remove symbolic link if it exists
if [ -L "/data/web_static/current" ]; then
	rm /data/web_static/current
fi

# Create symbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# Create or restore backup for sites-availabe/default
if [ -f /etc/nginx/sites-available/default.orig ]; then
	mv /etc/nginx/sites-available/default.orig /etc/nginx/sites-available/default
else
	sudo cp /etc/nginx/sites-available/default{,.orig}
fi

# Add location block
sudo sed -i "/server_name _/ a \\
	location \/hbnb_static {\\
		alias \/data\/web_static\/current\/;\\
	}" /etc/nginx/sites-available/default

sudo sed -i "/server_name jmkariuki.tech/ a \\
	location \/hbnb_static {\\
		alias \/data\/web_static\/current\/;\\
	}" /etc/nginx/sites-available/default

sudo service nginx restart
