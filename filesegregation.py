import os
import shutil

path="C:/Users/khann/OneDrive/Desktop/trash3"
names=os.listdir(path)

folder_name=['image','text']
for x in range(0,2):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for files in names:
    if '.jpeg' in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files, path+'image/'+files)
    if '.txt' in files and not os.path.exists(path+'text/'+files):
        shutil.move(path+files, path+'text/'+files)    
