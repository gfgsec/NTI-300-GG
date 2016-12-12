#bin/python

import os

def hello():
  print('Hi NTI300')
  print('This is Grants Python Install Script!')
  
hello()
  
def tree_install():
  print('Installing tree')
  os.system('sudo yum -y install tree')
  
tree_install()

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
  os.system('git clone https://github.com/grantypantyyy/NTI-300-GG.git')

clone_repo()

def publish_site():
  print('Publishing Website')
  os.system('sudo cp NTI-300-GG/webgrant.html /var/www/html')
  print('adjusting permisions')
  os.system('sudo chmod 644 /var/www/html/webgrant.html')
  os.system('sudo setenforce 0')
  os.system('sudo service httpd restart')
  
publish_site()

import subprocess

def install_django():
  os.chdir('NTI-300-GG')
  os.system('chmod +x django_install.sh')
  subprocess.call(['./django_install.sh'])
  
install_django()
  
  
  





















