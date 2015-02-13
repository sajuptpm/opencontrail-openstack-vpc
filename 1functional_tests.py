import os
import boto
import boto, boto.ec2
import unittest

class TestVPC(unittest.TestCase):
	def setUp(self):
		self.endpoint = os.environ['OS_HOST_IP']
		self.aws_access_key_id = os.environ['ADMIN_EC2_ACCESS_KEY']
		self.aws_secret_access_key = os.environ['ADMIN_EC2_SECRET_KEY']
		region = boto.ec2.regioninfo.RegionInfo(name="nova",endpoint=self.endpoint)
		self.conn = boto.connect_vpc(self.aws_access_key_id,
                        self.aws_secret_access_key,
                        is_secure=False,
                        region=region,
                        port=8773,
                        path="/services/Cloud")
		self.cidr = "10.0.0.0/24"
		self.vpc = None

	def test_create_vpc(self):
                vpc = self.conn.create_vpc(self.cidr)
		self.assertFalse(not vpc)

	def test_list_vpcs(self):
		vpcs = self.conn.get_all_vpcs()
		self.assertFalse(not vpcs)
	
	def test_delete_vpc(self):
                self.vpc = self.conn.create_vpc(self.cidr)
		res = self.conn.delete_vpc(self.vpc.id)
		self.assertTrue(True)
	
	def test_vpc_id_format(self):
		self.vpc = self.conn.create_vpc(self.cidr)
		self.assertTrue("vpc-" in self.vpc.id)		
	
	def tearDown(self):
		if self.vpc:
			try:
				self.conn.delete_vpc(self.vpc.id)
			except:
				pass


if __name__ == '__main__':
    unittest.main()
