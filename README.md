# Microservices Application

This repository contains two services:

- **Backend**: A Flask-based API that interacts with MongoDB.
- **Frontend**: A Flask-based web interface that communicates with the backend service.

---

## Prerequisites

- **MongoDB**: Installed locally.
- **Python 3.x**: Ensure you have Python 3 installed.
- **pip**: The Python package installer.

---

## MongoDB Setup

1. **Install MongoDB Locally**

   Follow the [MongoDB installation guide](https://docs.mongodb.com/manual/installation/) for your operating system.

2. **Start the MongoDB Service**

   If you're using WSL or a system that supports the `service` command, start MongoDB with:
   sudo service mongodb start

## Environment Variables
Both the backend and frontend services use environment variables for configuration. Create a .env file in each service directory with the following contents (adjust as needed):

# MongoDB settings
MONGO_HOST=localhost
MONGO_PORT=27017

# Backend settings
BACKEND_HOST=127.0.0.1
BACKEND_PORT=5001

# Frontend settings
FRONTEND_HOST=127.0.0.1
FRONTEND_PORT=5000

The applications use the python-dotenv package to load these variables.

## Running the Backend Service

1. **Navigate to the Backend Directory**
    cd backend

2. **Install Dependencies**
    pip install -r requirements.txt

3. **Start the Backend Application**
    python app.py

## Running the Frontend Service

1. **Navigate to the Frontend Directory**
    cd frontend

2. **Install Dependencies**
    pip install -r requirements.txt

3. **Start the Frontend Application**
    python app.py

4. **Access the Frontend Application**
    Open your web browser and go to:
    http://127.0.0.1:5000
    
## Additional Information

The backend service is responsible for handling API requests and interacting with the MongoDB database.

The frontend service sends requests to the backend and displays the results in a web interface.