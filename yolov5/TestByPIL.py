import os 
import torch 
from PIL import Image


cwd = os.getcwd()
model = torch.hub.load('ultralytics/yolov5', 'custom',path = cwd+"\\yolov5\\model\\last.pt",device="0")

img = Image.open('img\\test.png')
img = model(img)
img = img.render()[0]
img = Image.fromarray(img)
img.show()