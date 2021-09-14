def getBucket(storage_client,bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        return bucket
    except Exception as e:
        print(f"Bucket Not Found{e}")
        return 0
