#!/bin/bash

# Ensure the 'src' directory is in PYTHONPATH
export PYTHONPATH=$(pwd)/src

# Default host and port
HOST="127.0.0.1"
PORT="8000"

# Check if Uvicorn is installed
if ! command -v uvicorn &> /dev/null; then
    echo "Uvicorn is not installed. Installing..."
    pip install uvicorn fastapi
fi

# Run the FastAPI application
echo "Starting FastAPI server at http://$HOST:$PORT"
uvicorn src.api:app --host $HOST --port $PORT --reload