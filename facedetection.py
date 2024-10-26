
# image classification
# classifier:trained to identify faces by running them onto several thousands of images,then when it sees an image with a face , it can detect the face


# OpenCV library has a face detection classifier data stored in XML file format called as Haar Cascade Classifier

# Haar Cascade: Object detection Algorithm used to identify objects in an image or video


import cv2

img=cv2.imread(r"C:\Users\khann\OneDrive\Desktop\Assignments\cv\group.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade=cv2.CascadeClassifier(r'C:\Users\khann\OneDrive\Desktop\Assignments\cv\haarcascade_frontalface_default.xml')

faces=face_cascade.detectMultiScale(gray,1.1,2)
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),2)
cv2.imshow("img",img)
cv2.waitKey(0)
