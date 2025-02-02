# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Install system dependencies (if needed).
RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to leverage Docker cache.
COPY requirements.txt ./

# Install Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY app.py ./
COPY templates/ ./templates/

# Expose the port the app listens on.
EXPOSE 5000

# Define the command to run your app.
CMD ["python", "app.py"]
