#!/bin/bash

# format_code.sh
# This script runs the Black formatter on all Python files in the project.
# Ensures code consistency before committing changes.

# Set the directory (defaults to current directory if not specified)
PROJECT_DIR=${1:-$(pwd)}

# Check if Black is installed
if ! command -v black &> /dev/null; then
    echo "Black is not installed. Installing..."
    pip install black
fi

# Run Black formatter
echo "Formatting Python files in $PROJECT_DIR..."
black $PROJECT_DIR

echo "Code formatting complete."
