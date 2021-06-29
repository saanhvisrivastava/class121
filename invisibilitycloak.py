import cv2
import time
import numpy as np

fourcc=cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

cap=cv2.VideoCapture(0)
time.sleep(3)

bg=0

for i in range(60):
    ret,bg=cap.read()

#flip the background

bg=np.flip(bg,axis=1)# 1 is x 0 is y
 
while(cap.isOpened()):
    ret,image=cap.read()
    if not ret:
        break
    image=np.flip(image,axis=1)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])
    mask_1=cv2.inRange(hsv,lower_red,upper_red)

    lower_red=np.array([170,120,70])#bgr
    upper_red=np.array([180,255,255])
    mask_2=cv2.inRange(hsv,lower_red,upper_red)

    mask_1=mask_1+mask_2

    mask1=cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))#diff shape of array,3 by 3 metrix,uint datatypr into int
    mask1=cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    mask2=cv2.bitwise_not(mask_1)
    res_1=cv2.bitwise_and(image,image,mask=mask_2)#part of img without red

    res_2=cv2.bitwise_and(bg,bg,mask=mask_1)#bg with red

    final_output=cv2.addWeighted(res_1,1,res_2,1,0)#combine 2 imgs together,image 1 alpha img2 beta cam
    output_file.write(final_output)

    cv2.imshow('magic',final_output)
    cv2.waitKey(1)#binding func accept the value in milli second,return a char code for the currently pressed key,-1 if key not pressed

cap.release()
out.release()
cv2.destroyAllWindows()









    



#bgr into Heue(in the form of degree 120-green,0 red,240 blue)
# Saturation(encourse the intensity(diff shades)) and value(brightness)
