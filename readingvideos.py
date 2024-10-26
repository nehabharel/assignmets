# Video: FPS:Frames pre second: measure of how fast images are transitioning(40 fps:40images displayed in a second)

import cv2

#vid=cv2.VideoCapture(0) #if you want to use webcam

vid=cv2.VideoCapture("C:/Users/khann/OneDrive/Pictures/Camera Roll/WIN_20241022_18_07_44_Pro.mp4") #if you want to use uploaded video

if(vid.isOpened()==False):
    print("unable to read the feed")

height= int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width= int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps=int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

out=cv2.VideoWriter("Videoname.mp4",cv2.VideoWriter_Fourcc(*"DIVX"),30,(width,height))
while(True):
    ret,frame=vid.read()
    cv2.imshow("video display",frame)
    out.write(frame)
    if cv2.waitKey(20)==32:
         #number given to space key
         break
vid.release()
out.realease()    
cv2.destroyAllWindows()



