#!/usr/bin/env bash
# Deploying into my webserver web-01
sudo apt-get -y update
sudo apt-get -y install nginx

# creating the necessary folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# A fake html file for testing
echo "<html><head></head><body>Testing mic 1.2</body></html>" | sudo tee /data/web_static/releases/test/index.html

# creating or recreating the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Changing ownership
sudo chown -R ubuntu:ubuntu /data/

# updating nginx configuration
config_text="location /hbnb_static {\n\talias /data/web_static/current/;\n}\n"
sudo sh -c "echo '$config_text' > /etc/nginx/sites-available/default"

# then restarting nginx
sudo service nginx restart
