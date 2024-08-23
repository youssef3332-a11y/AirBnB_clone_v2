#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Install Nginx if it is not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get update -y
    sudo apt-get install nginx -y
fi

# Create the necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve content from /data/web_static/current/ to hbnb_static
nginx_conf="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static" $nginx_conf; then
    sudo sed -i "/server_name _;/ a \\
    location /hbnb_static {\\
        alias /data/web_static/current/;\\
    }" $nginx_conf
fi

# Restart Nginx to apply changes
sudo service nginx restart