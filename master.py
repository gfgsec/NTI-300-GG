#bin/python

import os

def hello():
  print('Hi NTI300')
  print('This is Grants Python Install Script!')
  
 hello()

def apache_install():
  print('Installing Apache Web Server')
  os.system('sudo yum -y install httpd')
  
  print('Starting http service')
  os.system('sudo systemctl enable httpd.service')
  
  print('Starting apache server')
  os.system('sudo systemctl start httpd.service')
  
  print('IMPORTANT! Create an inbound security rule to open port 80 on the server')
  
  
 apache_install()

def clone_repo():
  print('installing git')
  os.system('sudo yum -y install git')
  
  print('cloning Grants github repo')
  os.system('git clone https
