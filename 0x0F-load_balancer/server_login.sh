#!/bin/bash

#Define the server IPs and username
server1="54.84.76.212"
server2="3.85.54.208"
load_balancer="100.25.136.207"
username="ubuntu"

#prompt user to choose a server
echo "Choose a server to log in:"
echo "1. Web server 1 ($server1)"
echo "2. Web server 2 ($server2)"
echo "3. Load Balancer ($load_balancer)"
read -p "Enter your choice (1/2/3): " choice

# Display message before logging in
case $choice in
    1)
        echo "Connecting to Web server 1 ($server1) as $username..."
        ;;
    2)
        echo "Connecting to Web server 2 ($server2) as $username..."
        ;;
    3)
        echo "Connecting to Load Balancer ($load_balancer) as $username..."
        ;;
    *)
        echo "Invalid choice. Please enter a valid option."
        exit 1
        ;;
esac

#Perform SSH login based on your choice
case $choice in 
    1)
        ssh "$username@$server1"
        ;;
    2)
        ssh "$username@$server2"
        ;;
    3)
        ssh "$username@$load_balancer"
        ;;
esac