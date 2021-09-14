import Constants.Path

try:
    from google.cloud import storage
    from get_bucket import getBucket
    from Constants.Path import PATH
    import shutil
except Exception as e:
    print("Error : {} ".format(e))


def download_file(client,bucket_name,file_name="Orders.csv"):
    destination_file_name='DownLoad_'+file_name
    bucket=getBucket(client,bucket_name)
    if bucket:
        blob=bucket.blob(file_name)
        blob.download_to_filename(destination_file_name)
        src=f"{PATH}/DownLoad_{file_name}"
        dest=f"{PATH}/Downloads/DownLoad_{file_name}"
        shutil.move(src,dest)
        print("process commplete file download in the locals")
    else:
        print("bucket Not Found")

if __name__ == '__main__':
    client = storage.Client.from_service_account_json(json_credentials_path=f"{PATH}/gcp-assignment-322710-7ee5c22d656b.json")
    bucket_name = 'ag3-bucket'
    source_blob_name = 'Orders.csv'
    download_file(client,bucket_name,source_blob_name)

