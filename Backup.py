import os
import shutil
import datetime
import schedule
import time

# source_dir indicates the file,folder or directory you intend to move.
# destination_directory indicates the destination.
# 'r' converts the location path to a raw path to allow this program work successfully. 


source_dir= r'C:\Users\NGMC\Downloads\Xender\other'
destination_dir= r'C:\Users\NGMC\Desktop\Backups'

def copy_folder_to_directory(source,dest):
    today=datetime.date.today()
    des_dir=os.path.join(dest,str(today))

    try:
        shutil.copytree(source,des_dir)
        print(f'folder copied to: {dest}')
    except FileExistsError:
        print(f'folder already exists in: {dest}')

copy_folder_to_directory(source_dir,destination_dir)

    