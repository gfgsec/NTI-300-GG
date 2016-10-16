#!/bin/bash

echo "installing apache server"
sudo yum -y install httpd

echo "enabling apache server"
sudo systemctl enable httpd.service

echo "starting apache server"
sudo systemctl start httpd.service

echo "cloning branch from Grants github"
sudo git clone https://github.com/grantypantyyy/NTI-300-GG.git

echo "Bamboozeling an html file"
sudo mv NTI-300-GG/tree/website/grantweb.html /var/www/html

echo "Success!"
