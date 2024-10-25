# Python-3.12 Bookworm
FROM python:3.12.5-bookworm

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV PATH=/root/.local/bin:$PATH

# Update, install and configure system dependencies
RUN apt update && apt install dos2unix nginx -y && \
    python -m pip install --user pipx && \
    pipx install poetry && \
    poetry config virtualenvs.create false

# Copy to /app and set working directory
COPY . /app/.
WORKDIR /app

# Move and convert entrypoint, remove docker, install project
RUN mv /app/docker/entrypoint.sh /app/entrypoint.sh &&  \
    dos2unix /app/entrypoint.sh && \
    rm -rd docker && \
    poetry remove mkdocstrings-python && \
    poetry add mkdocstrings-python && \
    poetry install --without dev --no-cache && \
    python -m pip cache purge


# Expose port 80 and entrypoint
EXPOSE 80
ENTRYPOINT ["/app/entrypoint.sh"]
