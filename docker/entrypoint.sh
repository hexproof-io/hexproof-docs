#!/bin/bash

# Default domain
MKDOCS_BASE_URL=${MKDOCS_BASE_URL:-"https://hexproof.io"}

# Remove nginx defaults
echo 'Removing NGINX defaults ...'
service nginx stop || echo 'Failed to shutdown NGINX!'
rm -f /etc/nginx/conf.d/default.conf \
  && unlink /etc/nginx/sites-enabled/default \
  || echo 'Failed to remove NGINX defaults!'

# Generate documentation
hexdoc gen .
chmod 777 -R /app/projects

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
for dir in /app/projects/*; do
    project=$(basename "$dir")
    if [ "$project" != "main" ]; then
      cat <<EOL >> /etc/nginx/conf.d/nginx.conf
    location /$project {
        alias /app/projects/$project/site/;
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
        root /app/projects/main/site;
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