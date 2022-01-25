from tflite_runtime.interpreter import Interpreter
from SearchWindow import *
from tfapi import *
import cv2
import time


labels = load_labels(".\\labels\\labels.txt")
interpreter = Interpreter("\\model\\MapleStoryModel.tflite")

interpreter = Interpreter(interpreter)
interpreter.allocate_tensors()
_, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

hwnd = FindWindow_bySearch("MapleStory")
x, y, width, height = getWindow_W_H(hwnd)
freq = cv2.getTickFrequency()
while True:

    # FPS
    t1_fps = cv2.getTickCount()

    # load stream
    frame = getWindow_Img(hwnd)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (input_width, input_height))
    input_data = np.expand_dims(frame_resized, axis=0)
    t1 = time.monotonic()
    results = detect_objects(interpreter, input_data, 0.4)
    t2 = time.monotonic()
    f_result = draws_objects(frame, results, labels, width, height)
    t3 = time.monotonic()

    print("t2-t1",round(t2-t1,2))
    t2_fps = cv2.getTickCount()
    time1 = (t2_fps-t1_fps)/freq
    frame_rate_calc= 1/time1
    cv2.putText(frame,'FPS: {0:.2f}'.format(frame_rate_calc),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)

    cv2.imshow("screen box", f_result)
    # 關閉視窗
    k = cv2.waitKey(30)&0xFF #64bits! need a mask
    if k ==27:
        cv2.destroyAllWindows()
        break