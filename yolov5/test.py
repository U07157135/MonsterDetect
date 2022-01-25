from SearchWindow import getWindow_Img,FindWindow_bySearch
from time import sleep
import cv2
import os
import torch



hwnd = FindWindow_bySearch("dokidoki")
cwd = os.getcwd()
model = torch.hub.load('ultralytics/yolov5', 'custom',path = cwd+"\\yolov5\\model\\last.pt",device="0")


frame = getWindow_Img(hwnd)
frame = frame[...,:3] # BGRA to BGR
frame = frame[...,::-1] # BGR to RGB
frame = model(frame)
frame = frame.render()[0]
frame = frame[...,::-1] # RGB to RGB
cv2.imshow("screen box", frame)
k = cv2.waitKey(30)&0xFF #64bits! need a mask
if k ==27:
    cv2.destroyAllWindows()