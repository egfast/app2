#!/usr/bin/env bash

shutdown() {
	echo "Shutting down"
	echo "Killing app"
	kill $child_pid
	exit 0
}

trap shutdown SIGTERM SIGINT

echo "Starting entrypoint"
echo "Got arguments: $@"

python app.py $@ &
child_pid=$!
wait $child_pid
