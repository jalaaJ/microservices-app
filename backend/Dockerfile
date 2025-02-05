# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in the container.
WORKDIR /app

# Install system dependencies (if needed).
RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first to leverage Docker cache.
COPY requirements.txt ./

# Install Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code.
COPY app.py ./

# copy .env file if it exists
ARG ENV_FILE=.env
COPY ${ENV_FILE} .env

# Expose the port the app runs on.
EXPOSE 5001

# Define the command to run your app.
CMD ["python", "app.py"]
