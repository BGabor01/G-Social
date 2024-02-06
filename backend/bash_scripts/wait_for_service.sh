#!/bin/sh

# Function to check if a service is ready by trying to connect to a given host and port
wait_for_service() {
    local host=$1
    local port=$2
    echo "Waiting for $host to be ready..."
    while ! nc -z $host $port; do
        sleep 0.1
    done
    echo "$host is ready!"
}