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
  
  
 install_apache()
