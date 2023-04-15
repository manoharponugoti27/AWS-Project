import boto3
import os

# Set up AWS credentials
s3 = boto3.resource('s3')

import boto3


import boto3
import json
# create S3 bucket instance
#s3 = boto3.client('s3')
bucket_name = 'mybucketforwallpaper'
'''
s3.create_bucket(Bucket=bucket_name)
# define the policy
bucket_policy = {
     'Version': '2012-10-17',
     'Statement': [{
         'Sid': 'permission_statement',
         'Effect': 'Allow',
         'Principal': '*',
         'Action': ['s3:GetObject'],
         'Resource': "arn:aws:s3:::%s/*" % bucket_name
      }]
 }

'''


# Set up the name of your bucket and the folder containing the files you want to upload
#bucket_name = 'mydemobucket0'
folder_path = "C:\\Users\\umama\\OneDrive\\Desktop\\AWSProject\\Wallpapers"

# Iterate through all files in the folder and upload each one to S3
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    key_name = file_name
    s3.Bucket(bucket_name).upload_file(file_path, key_name)
    print(f'{file_name} uploaded to S3 bucket {bucket_name} as {key_name}')
