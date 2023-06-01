import os
import time

def backup_data(src_folder, dst_folder):
    # expand user home directory symbol ~ if used
    #src_folder = os.path.expanduser(src_folder)
    #dst_folder = os.path.expanduser(dst_folder)
    if not os.path.exists(src_folder):
        raise Exception("Source folder not found")

    
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    
    backup_name = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

    
    zip_file_name = f"{os.path.join(dst_folder, os.path.basename(src_folder))}_{backup_name}.zip"
    
    
    if os.system(f"zip -r {zip_file_name} {src_folder}") == 0:
        print(f"Backup of {src_folder} completed. Archive name: {zip_file_name}")
    else:
        print(f"Backup of {src_folder} failed.")
    
    #Optionally you can upload your buckup to a cloud env foe e.g. AWS S3  
    '''s3 = boto3.client('s3')

    #upload file to s3
    try:
        s3.upload_file(zip_file_name, bucket_name, os.path.basename(zip_file_name))
        print(f"Backup successfully uploaded to {s3_bucket_name}")
    except Exception as e:
        print(f"Failed to upload backup to AWS S3: {e}")'''



# replace '/path/to/directory/' with the path of the folder you want to backup
# replace '/path/to/destination/' with the path of the folder where you want to save the backup
backup_data('/path/to/directory/', '/path/to/destination/') #add s3_bucket_name if you want  

