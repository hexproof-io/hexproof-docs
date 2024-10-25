# Nginx Bookworm
FROM nginx:stable

# Copy to /app and set working directory
COPY docker/entrypoint.sh /app/entrypoint.sh
COPY projects/main/repo/site /sites/main
COPY projects/hexproof/repo/site /sites/hexproof
COPY projects/hexproof-api/repo/site /sites/hexproof-api
COPY projects/mtg-vectors/repo/site /sites/mtg-vectors
COPY projects/proxyshop/repo/site /sites/proxyshop
WORKDIR /app

# Expose port 80 and entrypoint
EXPOSE 80
ENTRYPOINT ["/app/entrypoint.sh"]
