#!/usr/bin/env bash
# uninstalls Nginx and removes its configuration

service nginx stop
apt-get -y remove --purge nginx
apt-get -y autoremove
apt-get -y autoclean

# Optional: Remove Nginx configuration files
rm -rf /etc/nginx

# Optional: Remove Nginx logs
rm -rf /var/log/nginx

# Optional: Remove Nginx web root directory
rm -rf /var/www/html

# Optional: Remove any remaining Nginx-related packages
apt-get -y remove --purge nginx-*

echo "Nginx has been successfully uninstalled."

