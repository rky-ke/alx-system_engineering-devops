#!/bin/bash

echo "SSH Login Script"

private_key_path="/root/.ssh/id_rsa"

server_ip="34.229.55.201"
username="ubuntu"

echo "Connecting to the remote server..."
ssh -i "$private_key_path" "$username@$server_ip"

