#!/bin/bash

# Function to handle cleanup on exit
cleanup() {
  echo "Stopping services..."

  # Kill backend and frontend processes if they're running
  if [ -n "$BACKEND_PID" ]; then
    echo "Killing Backend process (PID: $BACKEND_PID)..."
    kill $BACKEND_PID
  fi

  if [ -n "$FRONTEND_PID" ]; then
    echo "Killing Frontend process (PID: $FRONTEND_PID)..."
    kill $FRONTEND_PID
  fi

  # Stop MongoDB service
  echo "Stopping MongoDB service..."
  sudo service mongodb stop

  exit 0
}

# Trap SIGINT and SIGTERM signals to run cleanup
trap cleanup SIGINT SIGTERM

# Start MongoDB service
echo "Starting MongoDB service..."
sudo service mongodb start

# Wait a few seconds to ensure MongoDB starts properly
sleep 5

# Start the Backend service
echo "Starting Backend service..."
cd backend || { echo "Backend directory not found"; exit 1; }

# Uncomment the next line to install dependencies each time:
# pip install -r requirements.txt

python app.py &
BACKEND_PID=$!
cd ..

# Start the Frontend service
echo "Starting Frontend service..."
cd frontend || { echo "Frontend directory not found"; exit 1; }

#Uncomment the next line to install dependencies each time:
# pip install -r requirements.txt

python app.py &
FRONTEND_PID=$!
cd ..

echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo "All services started. Press Ctrl+C to stop."

# Wait indefinitely until a termination signal is received
wait
