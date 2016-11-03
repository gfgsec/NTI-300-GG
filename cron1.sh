#!/bin/bash

users=$( /usr/bin/who | grep -c "" )

echo "number of users loged in is $users"

if [ "$users" -gt "1" ]; then
    echo "there's more than one user logged in"
  else
    echo "There's 1 or less user logged in"
fi
