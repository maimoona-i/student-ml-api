FROM python:3.11-slim

# Build-time metadata (passed in from CI/release workflow)
ARG APP_VERSION=1.0.0
ARG GIT_COMMIT=unknown
ARG BUILD_DATE=unknown

# OCI-standard image labels for traceability (Part 23)
LABEL org.opencontainers.image.title="student-ml-api" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${GIT_COMMIT}" \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.source="https://github.com/<your-username>/student-ml-api"

WORKDIR /app

# Copy dependency manifest FIRST so this layer is cached and reused
# whenever only app.py changes (Part 25).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application code changes most often, so it goes in its own layer LAST.
COPY app.py .
COPY VERSION .

EXPOSE 5000

# Bind to 0.0.0.0, NOT 127.0.0.1 - required for the API to be
# reachable from outside the Docker container (see Part 26).
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
