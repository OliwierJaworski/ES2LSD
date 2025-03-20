#!/bin/bash

# Path to your virtual environment
VENV_DIR="/home/patrick/Desktop/elektronische_systemen/.venv"
MAIN_PY="/home/patrick/Desktop/elektronische_systemen/main.py"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
  echo "Virtual environment not found. Please create it first."
  exit 1
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Run the main.py script
python "$MAIN_PY"

# Deactivate the virtual environment after running the script
deactivate