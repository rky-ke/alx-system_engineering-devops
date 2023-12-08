#!/bin/bash

echo "SSH Login Script"
server_ip="34.224.5.232"
username="ubuntu"

echo "Connecting to the remote server..."
ssh "$username@$server_ip"

