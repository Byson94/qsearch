#!/bin/bash

YELLOW="\033[1;33m"
NC="\033[0m"

echo -e "${YELLOW}DEBUG ONLY:${NC} This script is intended for testing and debugging purposes."
echo -e "Do not use it to install the program system-wide."
echo -e "To properly install, run:"
echo -e "  ${YELLOW}makepkg -si${NC}"
echo -e "Avoid manually copying files to system directories (e.g., ${YELLOW}sudo cp ./qsearch.pyz /usr/bin/qsearch${NC})."
echo -e "Using the package manager ensures proper installation, dependencies, and future updates.\n"

shiv -e qsearch.main:main -o qsearch.pyz -r src/raw_requirements.txt .