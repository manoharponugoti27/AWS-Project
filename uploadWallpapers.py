import boto3
import os
import mysql.connector
import datetime
import time

current_time = datetime.datetime.now()

# Set up AWS credentials
s3 = boto3.resource('s3')

import boto3

# create S3 bucket instance
#s3client = boto3.client('s3')
bucket_name = 'mybucketforwallpaper'
'''
s3client.create_bucket(Bucket=bucket_name)
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

def upload_images(folder_path):
# Iterate through all files in the folder and upload each one to S3
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        key_name = file_name
        s3.Bucket(bucket_name).upload_file(file_path, key_name)
        print(f'{file_name} uploaded to S3 bucket {bucket_name} as {key_name}')


def insert_data():
    s3 = boto3.resource('s3')
    bucket_name = 'mybucketforwallpaper'

    bucket = s3.Bucket(bucket_name)
    mydb = mysql.connector.connect(
    host = "my-rds-instance.cb3awmiitwm0.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "mypassword",
    database = "mydatabase"
    )
    for obj in bucket.objects.all():
                # Generate a presigned URL for the object
        url = s3.meta.client.generate_presigned_url(
                    'get_object',
                    Params={
                        'Bucket': bucket_name,
                        'Key': obj.key
                    }
                )

                #wallpapers.append(url)
                #filenames.append(filenames)
                # Print the URL
        print(url)

                # Query the RDS database for the download counts of each wallpaper
        mycursor = mydb.cursor()
        mycursor1 = mydb.cursor()

        sql = "INSERT INTO wallpapers (FileName, bucket_name,path,create_time) VALUES (%s,%s,%s,%s)"
        val = (obj.key, bucket_name,url,current_time)

        mycursor.execute(sql, val)
        mydb.commit()
    print(mycursor.rowcount)

upload_images(folder_path)

#adding delay to the code
time.sleep(10)

insert_data()
