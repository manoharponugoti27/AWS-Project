import boto3

s3 = boto3.resource('s3')
bucket_name = 'mybucketforwallpaper'

bucket = s3.Bucket(bucket_name)

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

    # Print the URL
    print(url)
