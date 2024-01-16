#!/bin/bash

echo "SSH Login Script"
server_ip="54.84.76.212"
username="ubuntu"

echo "Connecting to the remote server..."
ssh "$username@$server_ip"

