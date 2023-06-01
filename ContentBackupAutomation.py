import os
import time

def backup_data(src_folder, dst_folder):
    
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

# replace '/path/to/directory/' with the path of the folder you want to backup
# replace '/path/to/destination/' with the path of the folder where you want to save the backup
backup_data('/path/to/directory/', '/path/to/destination/')

