import os 
import torch 
import cv2


cwd = os.getcwd()
model = torch.hub.load('ultralytics/yolov5', 'custom',path = cwd+"\\yolov5\\model\\last.pt",device="0")

img = cv2.imread("yolov5\\img\\test.png")
img = img[..., ::-1]
img = model(img)
img = img.render()[0]
img = img[..., ::-1]
cv2.imshow("screen box", img)
k = cv2.waitKey(0)
if k ==27:
    cv2.destroyAllWindows()