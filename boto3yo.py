#!/bin/python

import boto3
import base64
import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

amazon_image = 'ami-6f68cf0f'                                       # This will launch a red hat instance
amazon_instance = 't2.micro'                                        # we've been working with micro's, if you use Amizon Linux, you could launch a nono
amazon_pem_key = 'NTI300'                    # the name of the key/pem file you would like to use to access this machine
firewall_profiles = ['default']                             # the security group name(s) you would like to use, remember, this is your firewall, make sure the ports you want open are open

print(amazon_image)
print(amazon_instance)
print(amazon_pem_key)

def launch_test_instance():

   instances = ec2.create_instances(
      ImageId = amazon_image,
      InstanceType = amazon_instance,
      MinCount=1,
      MaxCount=1,
      KeyName = amazon_pem_key,
      SecurityGroupIds = firewall_profiles,
      UserData="""#!/bin/python

import os
import subprocess

def hello():
  print('Hi NTI300')
  print('This is Grants Python Install Script!')
  
hello()
  
def tree_install():
  print('Installing tree')
  os.system('yum -y install tree')
  
tree_install()

def apache_install():
  print('Installing Apache Web Server')
  os.system('yum -y install httpd')
  
  print('Starting http service')
  os.system('systemctl enable httpd.service')
  
  print('Starting apache server')
  os.system('systemctl start httpd.service')
  
  print('IMPORTANT! Create an inbound security rule to open port 80 on the server')
  
apache_install()

def clone_repo():
  print('installing git')
  os.system('yum -y install git')
  
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

def setup_install():
   print('installing pip and virtualenv so we can give django its own version of python')
   os.system('rpm -iUvh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm')
   os.system('yum -y install python-pip && pip install --upgrade pip')
   os.system('pip install virtualenv')
   os.chdir('/opt')
   os.mkdir('/opt/django')
   os.chdir('/opt/django')
   os.system('virtualenv django-env')
   os.system('chown -R ec2-user /opt/django')   # we're useing shell, because the python builtin chown is kind of lame in this case

def django_install():
   print('activating virtualenv and installing django after pre-requirements have been met')
   # You must activate the virtualenv shell every time you perform a command in order for it to work from python.
   os.system('source /opt/django/django-env/bin/activate && pip install django')
   # confirm install and start a django project
   os.chdir('/opt/django')
   os.system('source /opt/django/django-env/bin/activate ' + \
             '&& django-admin --version ' + \
             '&& django-admin startproject project1')

def django_start():
   print('starting django')
   os.system('source /opt/django/django-env/bin/activate && python /opt/django/project1/manage.py runserver 0.0.0.0:8000&')

setup_install()
django_install()
django_start()

def mailx():
    print('Installing mailx')
    os.system('yum -y install mailx')

mailx()

def crontab():
    print('Creating crontab entry for Server Alert emails every 30 minutes.')
    os.system('sudo chmod +x /home/ec2-user/NTI-300-GG/cron2.sh')
    os.system('(crontab -l 2>/dev/null; echo "0,30 * * * * /home/ec2-user/NTI-300-GG/cron2.sh | mail -s \"Server Alert\" grantgrismore@outlook.com") | crontab - ')
    os.system('crontab -l')

crontab()

def update_kernel():
  print('Updating kernal')
  os.system('yum clean all && yum update kernel -y')
  print('Done!')
  print('Verifying dirty cow patch')
  os.system('rpm -q --changelog kernel | grep CVE-2016-5195')
  
update_kernel()

def awscli():
    print('Installing the AWS CLI')
    os.system('pip install -y awscli')

awscli()

def boto3():
    print('Installing Boto3')
    os.system('pip install -y boto3')
    print('Install Script Complete! AWS RHEL Server ready to use.')
  
boto3()"""

    )

   pprint.pprint(instances)


launch_test_instance()
