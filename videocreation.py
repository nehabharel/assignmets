import cv2
import os
path="images"

images=[]


for file in os.listdir(path):
    name,ext=os.path.splitext(file)
    if ext in ['.gif','.png','.jpg','.jpeg']:
        file_name=path+ "/"+file
        images.append(file_name)
count=len(images)

# using videowriter creat a video using the images