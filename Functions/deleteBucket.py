
def delete_bucket(client,bucketName):
    try:
        bucket=client.bucket(bucketName)
        bucket.delete()
        print("bucket Deleted")
    except Exception as e:
        print("Bucket can't Delete ",e)