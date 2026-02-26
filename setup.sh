#!/bin/bash

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Please source this script: source $0"
    exit 1
fi

VENV_DIR="./venv"

# Check if venv already exists
if [[ -d "$VENV_DIR" ]]; then
    echo "Virtual environment already exists."
else
    echo "=== Setting up Venv ==="
    python -m venv "$VENV_DIR"
    echo Done!
fi

# Check if we are already in a venv
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "=== Activating Venv ==="
    source "$VENV_DIR/bin/activate"
    echo Done!
else
    echo "Already inside a virtual environment: $VIRTUAL_ENV"
fi

# Check if pip is available
if command -v pip >/dev/null 2>&1; then
    echo "=== Installing Dependencies ==="
    pip install -r requirements.txt
else
    echo "pip not found. Is the virtual environment activated?"
fi