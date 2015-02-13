
import os
import boto
import boto, boto.ec2

region = boto.ec2.regioninfo.RegionInfo(name="nova",endpoint=os.environ['OS_HOST_IP'])

conn = boto.connect_vpc(aws_access_key_id=os.environ['ADMIN_EC2_ACCESS_KEY'],
                        aws_secret_access_key=os.environ['ADMIN_EC2_SECRET_KEY'],
                        is_secure=False,
                        region=region,
                        port=8773,
                        path="/services/Cloud")


def create_vpc():
        cidr = raw_input("\nEnter CIDR [10.0.0.0/24]  : ")
        vpc = conn.create_vpc(cidr)
        return vpc

def list_vpcs():
        return conn.get_all_vpcs()

def create_subnet():
	vpc_id = raw_input("\nEnter VPC Id [vpc-db6531ce]  : ")
	cidr = raw_input("\nEnter CIDR [10.0.0.0/24]  : ")
	return conn.create_subnet(vpc_id, cidr)

def list_subnets():
        return conn.get_all_subnets()


while True:
	res = raw_input("\nEnter the action [create-vpc, list-vpcs, create-subnet, list-subnets]  : ")

	if res in ['create-vpc']:
		print create_vpc()	
	if res in ['list-vpcs']:
		print list_vpcs()		
        if res in ['create-subnet']:
                print create_subnet()
        if res in ['list-subnets']:
                print list_subnets()










