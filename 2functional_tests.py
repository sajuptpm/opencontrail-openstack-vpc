import os
import boto
import boto, boto.ec2
import unittest

class TestVPCOperations(unittest.TestCase):
        def setUp(self):
                self.endpoint = os.environ['OS_HOST_IP']
                self.aws_access_key_id = os.environ['VPC_USER_EC2_ACCESS_KEY']
                self.aws_secret_access_key = os.environ['VPC_USER_EC2_SECRET_KEY']
                region = boto.ec2.regioninfo.RegionInfo(name="nova",endpoint=self.endpoint)
                self.conn = boto.connect_vpc(self.aws_access_key_id,
                        self.aws_secret_access_key,
                        is_secure=False,
                        region=region,
                        port=8773,
                        path="/services/Cloud")
                self.cidr = "10.0.0.0/24"

        def test_create_subnet(self):
                self.vpc = self.conn.create_vpc(self.cidr)

        def tearDown(self):
                pass


if __name__ == '__main__':
    unittest.main()

