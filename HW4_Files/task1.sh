#!/bin/bash

# Find the PIDs of infinite.sh
PIDS=$(ps aux | grep '[i]nfinite.sh' | awk '{print $2}')

# Check if any process is found
if [ -n "$PIDS" ]; then
    for PID in $PIDS; do
        echo "Killing process infinite.sh with PID: $PID"
        kill "$PID"
    done
else
    echo "No infinite.sh process found."
fi
