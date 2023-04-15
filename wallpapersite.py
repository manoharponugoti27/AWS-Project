from flask import Flask, render_template, send_file
import boto3
import os
import pymysql

app = Flask(__name__)

# AWS S3 bucket name and region
BUCKET_NAME = 'mybucketforwallpaper'
REGION_NAME = 'us-east-1'

# AWS RDS database configuration
DB_HOST = 'my-rds-instance.cb3awmiitwm0.us-east-1.rds.amazonaws.com'
DB_PORT = 3306
DB_NAME = 'mydatabase'
DB_USER = 'admin'
DB_PASSWORD = 'mypassword'

# Connect to the RDS database
#conn = pymysql.connect(host=DB_HOST, port=DB_PORT, db=DB_NAME, user=DB_USER, password=DB_PASSWORD)

@app.route('/')
def index():
    # Get a list of all wallpapers from S3 bucket
    '''s3 = boto3.client('s3', region_name=REGION_NAME)
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    print(response)
    wallpapers = [obj['Key'] for obj in response['Contents']]
    print(wallpapers)'''
    import boto3

    s3 = boto3.resource('s3')
    bucket_name = 'mybucketforwallpaper'

    bucket = s3.Bucket(bucket_name)

    wallpapers= []
    # Iterate through all objects in the bucket
    for obj in bucket.objects.all():
        # Generate a presigned URL for the object
        url = s3.meta.client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': obj.key
            }
        )
        wallpapers.append(url)

        # Print the URL
        print(url)

        # Query the RDS database for the download counts of each wallpaper
        #cursor = conn.cursor()
        #cursor.execute('SELECT filename, downloads FROM wallpapers')
        #download_counts = {row[0]: row[1] for row in cursor.fetchall()}
    
    return render_template('index.html', wallpapers=wallpapers)#, download_counts=download_counts)

@app.route('/wallpapers/<filename>')
def wallpaper(filename):
    # Increment the download count of the requested wallpaper in the RDS database
    #cursor = conn.cursor()
    #cursor.execute('UPDATE wallpapers SET downloads = downloads + 1 WHERE filename = %s', (filename,))
    #conn.commit()
    
    # Download the requested wallpaper from S3 bucket and return it as a file
    s3 = boto3.client('s3', region_name=REGION_NAME)
    response = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
    return send_file(response['Body'], attachment_filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
