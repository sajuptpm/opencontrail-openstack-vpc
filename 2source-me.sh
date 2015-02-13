
export OS_HOST_IP=192.168.56.102
export OS_USERNAME=admin
export OS_PASSWORD=secret123
export OS_TENANT_NAME=admin
export OS_AUTH_URL=http://$OS_HOST_IP:35357/v2.0


VPC_ID=vpc-a2825469
USER_NAME="use3"
TENANT_LIST=$(keystone tenant-list)
TENANT_ID=$(echo "$TENANT_LIST" | awk  "/ $VPC_ID /" | awk '{ print $2 }')
ROLE_LIST=$(keystone role-list)
ADMIN_ROLE_ID=$(echo "$ROLE_LIST" | awk '/ admin / { print $2 }')
CREATE_USER=$(keystone user-create --name $USER_NAME --tenant $TENANT_ID --pass password --enabled true)
USER_ID=$(echo "$CREATE_USER" | awk '/ id / { print $4 }')
USER_ROLE_ADD=$(keystone user-role-add --user $USER_ID --role $ADMIN_ROLE_ID --tenant $TENANT_ID)
$(echo "$USER_ROLE_ADD")
EC2_CRED_CRE=$(keystone ec2-credentials-create --user-id $USER_ID --tenant-id $TENANT_ID)
VPC_USER_EC2_ACCESS_KEY=$(echo "$EC2_CRED_CRE" | awk '/ access / { print $4 }')
VPC_USER_EC2_SECRET_KEY=$(echo "$EC2_CRED_CRE" | awk '/ secret / { print $4 }')

