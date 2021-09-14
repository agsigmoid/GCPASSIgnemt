def create_bucket(client,bucketName):
    try:

        bucket=client.bucket(bucketName)
        bucket.create();
        return bucket
    except Exception as e:
        print(f"bucket can't create{e}")
        return 0
