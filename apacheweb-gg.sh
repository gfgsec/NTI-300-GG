#!/bin/bash

echo "installing apache server"
sudo yum -y install httpd

echo "enabling apache server"
sudo systemctl enable httpd.service

echo "starting apache server"
sudo systemctl start httpd.service

echo "cloning branch from Grants github"
sudo yum -y install git
sudo git clone https://github.com/grantypantyyy/NTI-300-GG.git

echo "publishing content"
sudo cp NTI-300-GG/webgrant.html /var/www/html

echo "adjusting permissions"
sudo chmod 644 /var/www.html/webgrant.html
sudo setenforce 0
