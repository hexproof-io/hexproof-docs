#!/bin/bash

# Create base nginx configuration
cat <<EOL > /etc/nginx/conf.d/nginx.conf
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # Enable gzip compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml image/svg+xml;
    gzip_proxied any;
    gzip_min_length 256;
    gzip_comp_level 6;
    gzip_buffers 16 8k;
    gzip_vary on;

    # Redirect logs to stdout and stderr
    access_log /dev/stdout;
    error_log /dev/stderr;

EOL

# Add each project to nginx configuration
for dir in /sites/*; do
    project=$(basename "$dir")
    if [ "$project" != "main" ]; then
      cat <<EOL >> /etc/nginx/conf.d/nginx.conf
    location /$project {
        alias /sites/$project/;
        index index.html;
        if (\$request_uri ~ ^/(.*)\.html(\?|$)) {
            return 302 /$1;
        }
        try_files \$uri \$uri/ =404;
    }

EOL
    fi
done

# Finalize and print nginx configuration
cat <<EOL >> /etc/nginx/conf.d/nginx.conf
    location / {
        root /sites/main;
        index index.html;
        if (\$request_uri ~ ^/(.*)\.html(\?|$)) {
            return 302 /$1;
        }
        try_files \$uri \$uri/ =404;
    }

}
EOL

# Start nginx
echo "Starting Nginx ..."
nginx -g 'daemon off;'