#!/bin/bash

echo "SSH Key Generation Script"

read -p "Enter your email address: " email

echo "Generating SSH key pair..."
ssh-keygen -t rsa -b 4096 -C "$email"

echo "SSH key pair generated successfully."

