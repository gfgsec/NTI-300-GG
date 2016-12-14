#!/usr/bin/python

import boto3
import base64
import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

amazon_image = 'ami-2051294a'                                       # This will launch a red hat instance
amazon_instance = 't2.micro'                                        # we've been working with micro's, if you use Amizon Linux, you could launch a nono
amazon_pem_key = 'load-ballancer-static-content'                    # the name of the key/pem file you would like to use to access this machine
firewall_profiles = ['launch-wizard-2']                             # the security group name(s) you would like to use, remember, this is your firewall, make sure the ports you want open are open

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
      UserData="""#!/usr/bin/python
import sys, os
# your script here... I don't want to see my exact script or my repo

def set_up_git():
   print('install git')
   os.system('yum -y install git')
   
   print('instally my reposoitory')
   os.system('git clone https://github.com/nic-instruction/python_deploy.git /tmp/python_deploy')

set_up_git()

sys.path.append('/tmp/python_deploy')

import app_install

app_install.install_apache()

"""

    )

   pprint.pprint(instances)


launch_test_instance()
