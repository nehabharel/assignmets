#computer vision :CV: help the computer to identify and understand the digital content
#  pixels: digital image stored as a set of numbers// tiny dots on computer display aranged in rows and column 


#Binary images:back and white images(0:black, 1:white), 
# gray-scale images: monochrome images /one coloured images (0-255)
#colored image: 3 bands /channels :red band(0-255), green band(0-255), blue(0-255)


# openCV
#pip install opencv-python

import cv2 

img=cv2.imread("C:/Users/khann/OneDrive/Desktop/trash1/download.png")

cv2.imshow("Display image",img)

gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print(img)
cv2.waitKey(0)


#in open cv coloured images are represented as BGR band
