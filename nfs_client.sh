# use ifconfig to find your IP address, you will use this for the client.

From the client (ubuntu machine)

apt-get install nfs-client

showmount -e $ipaddress # where $ipaddress is the ip of your nfs server
mkdir /mnt/test 
echo "10.128.0.4:/var/nfsshare/testing        /mnt/test       nfs     defaults 0 0" >> /etc/fstab
mount -a
*profit*
