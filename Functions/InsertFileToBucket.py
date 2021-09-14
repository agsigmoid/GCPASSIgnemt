from get_bucket import getBucket
def Upload_file_to_bucket(client,bucketName,file_name):
    try:
        bucket=getBucket(client,bucketName)
        if(bucket):
            object1 = bucket.blob(file_name)
            object1.upload_from_filename(f"/Users/Agam_Gupta/Desktop/Sigmoid/GCPAssign/{file_name}")
            print(f"{file_name} is stored in {bucketName}")
        else:
            print("no Bucket Found")
    except Exception as e:
        print("error in upload file",e)