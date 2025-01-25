# pusher-client-python/Dockerfile
FROM python:3.11-slim


# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "client.py"]