#!/bin/bash

echo "SSH Login Script"
server_ip="100.24.242.252"
username="ubuntu"

echo "Connecting to the remote server..."
ssh "$username@$server_ip"

