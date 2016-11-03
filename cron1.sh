#!/bin/bash

users=$( /usr/bin/who | grep -c "" )

echo "number of users loged in is $users"

if [ "$users" -gt "0" ]; then
    echo "there's more than one user logged in"
  else
    echo "There are no users logged in" | mail -s "There are no users logged into your Red Hat Instance" grant.grismore@seattlecolleges.edu
fi
