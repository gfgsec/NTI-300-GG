#!/bin/bash

timer=$(cat /proc/uptime | cut -d " " -f1)
users=$(/usr/bin/who | grep -c "")

if [ "$timer" > "7200" ]; then
    echo "Server `hostname` Server ALERT!"
    echo "Number of users logged on: $users"
    echo -e "Server Alert: `hostname`:\n `uptime -p` \n USERS: `who` "

else
    exit 0

fi

if [ "$users" -ge "1" ]; then
    echo "There are users logged on."

else
    echo "There are no users logged on."

fi
