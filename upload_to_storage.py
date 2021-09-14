try:
    from google.cloud import storage
    import google.cloud.storage
    import json
    import os
    # To check Bucket Exist or Not if not return 0 elese return Bucket
    from Functions.get_bucket import getBucket
    # To create New Bucket
    from Functions.Create_Bucket import create_bucket
    # to insert File into Bucket
    from Functions.InsertFileToBucket import Upload_file_to_bucket
    # check Bucket exist if yes it will Delete that bucket
    from Functions.deleteBucket import delete_bucket
    from Constants.Path import PATH
    import sys
except Exception as e:
    print("Error : {} ".format(e))

client=storage.Client.from_service_account_json(json_credentials_path=f'{PATH}/gcp-assignment-322710-7ee5c22d656b.json')


def files_in_bucket(client,bucket_name):
    ''' gets all the files in Bucket'''
    bucket=getBucket(client,bucket_name)
    blobs=bucket.list_blobs()
    for blob in blobs:
        print(blob.name);

def TotalBuckets(client):
    '''print Total number of buckets in the Conatiner'''
    buckets = client.list_buckets()
    for bucket in buckets:
        print(bucket.name)
        # bucket1=getBucket(client,bucket)
        files_in_bucket(client,bucket.name)


# TotalBuckets(client)

# to insert File into Bucket
Upload_file_to_bucket(client,'ag3-bucket','Orders.csv')
Upload_file_to_bucket(client,'ag3-bucket','Customers.csv')
#
# # gets all the files in Bucket
files_in_bucket(client,'ag3-bucket')


#uset to create Bucket
if(create_bucket(client,'ag1213-bucket')):
    print("bucket created")
else:
    print("Bucket is not Created")


# Delete Bucket
delete_bucket(client,'ag1213-bucket')
