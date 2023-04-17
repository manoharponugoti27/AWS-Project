from flask import Flask, render_template, send_file
import boto3
import json
import mysql.connector
import datetime;
 
# ct stores current time
ct = datetime.datetime.now()

app = Flask(__name__)

# AWS S3 bucket name and region
BUCKET_NAME = 'mybucketforwallpaper'
REGION_NAME = 'us-east-1'

# AWS RDS database configuration
# Connect to the RDS database
mydb = mysql.connector.connect(
  host = "my-rds-instance.cb3awmiitwm0.us-east-1.rds.amazonaws.com",
  user = "admin",
  password = "mypassword",
  database = "mydatabase"
)



@app.route('/')
def index():
    try:
    # Get a list of all wallpapers from S3 bucket
        
        '''import boto3

        s3 = boto3.resource('s3')
        bucket_name = 'mybucketforwallpaper'

        bucket = s3.Bucket(bucket_name)
        s3client = boto3.client('s3')'''
        wallpapers= []
        # Iterate through all objects in the bucket
        
        query = "SELECT path FROM wallpapers"
        mycursor1 = mydb.cursor()
        mycursor1.execute(query)
        myresult = mycursor1.fetchall()
        print(myresult)
        for x in myresult:
           wallpapers.append(x[0])
        print(wallpapers)
        
        #print(fileList)
        return render_template('index.html', wallpapers=wallpapers)#, download_counts=download_counts)
    except:
        print("error")

'''@app.route('/wallpapers/<filename>')
def wallpaper(filename):
    # Increment the download count of the requested wallpaper in the RDS database
    #cursor = conn.cursor()
    #cursor.execute('UPDATE wallpapers SET downloads = downloads + 1 WHERE filename = %s', (filename,))
    #conn.commit()
    
    # Download the requested wallpaper from S3 bucket and return it as a file
    s3 = boto3.client('s3', region_name=REGION_NAME)
    response = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
    return send_file(response['Body'], attachment_filename=filename)'''

if __name__ == '__main__':
    app.run(debug=False)
