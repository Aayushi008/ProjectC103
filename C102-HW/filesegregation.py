import os
import shutil
from_dir="/Users/aayushisinghal/Downloads"
to_dir="/Users/aayushisinghal/Desktop/Python Coding/C102"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, ext=os.path.splitext(file_name)
    print(name, ext)
    if ext=="":
        continue
    if ext in ['.txt', '.doc','docx','.pdf']:
        path1= from_dir+"/"+file_name
        path2=to_dir+"/"+"image_files"
        path3=path2+"/"+file_name
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1, path3)