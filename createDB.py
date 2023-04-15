import boto3
rds_client = boto3.client('rds', region_name='us-east-1')


instance_name = 'my-rds-instance'
db_name = 'mydatabase'
db_username = 'admin'
db_password = 'mypassword'
db_instance_class = 'db.t2.micro'
db_engine = 'mysql'
allocated_storage = 20

response = rds_client.create_db_instance(DBInstanceIdentifier=instance_name,
                                         AllocatedStorage=allocated_storage,
                                         DBInstanceClass=db_instance_class,
                                         Engine=db_engine,
                                         MasterUsername=db_username,
                                         MasterUserPassword=db_password,
                                         DBName=db_name)

response = rds_client.describe_db_instances(DBInstanceIdentifier=instance_name)
instance_status = response['DBInstances'][0]['DBInstanceStatus']
