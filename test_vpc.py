
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

#print conn.get_all_vpcs()
#print conn.get_all_regions()
