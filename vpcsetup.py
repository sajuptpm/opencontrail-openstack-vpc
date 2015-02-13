
import os
from keystoneclient.v2_0 import client

def setup(vpc_id="a2"):
	keystone = client.Client(username=os.environ['OS_USERNAME'], 
		password=os.environ['OS_PASSWORD'], 
		auth_url=os.environ['OS_AUTH_URL'],
		tenant_name=os.environ['OS_TENANT_NAME'])
	
	tenants = keystone.tenants.list()
	for tenant in tenants:
		if tenant.name in [vpc_id]:
			break

	user = keystone.users.create(name=vpc_id, password='password', tenant_id=tenant.id, enabled=True)

	roles=keystone.roles.list()	
	for role in roles:
		if role.name in ['admin']:
			break
	keystone.roles.add_user_role(user, role, tenant)
	ec2key = keystone.ec2.create(user_id=user.id, tenant_id=tenant.id)
	os.environ['VPC_USER_EC2_ACCESS_KEY'] = ec2key.access
	os.environ['VPC_USER_EC2_SECRET_KEY'] = ec2key.secret

#setup()

#if __name__ == '__main__':
#	main()
