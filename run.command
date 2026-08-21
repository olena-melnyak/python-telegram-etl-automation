#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 main.py

echo
echo "======================================"
echo "Pipeline completed."
echo "Press Enter to close..."
read
