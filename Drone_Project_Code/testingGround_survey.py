import cv2
from djitellopy import tello
import cvzone

thres = 0.55
nmsThres = 0.2

classNames = []
classFile = 'Drone_Project_Code/coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')
print(classNames)
configPath = 'Drone_Project_Code/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = "Drone_Project_Code/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamoff()
me.streamon()

'''
me.takeoff()
me.move_up(80)
'''

while mode == "tracking":
    # success, img = cap.read()
    img = me.get_frame_read().frame
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres)
    try:
        for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cvzone.cornerRect(img, box)
            cv2.putText(img, f'{classNames[classId - 1].upper()} {round(conf * 100, 2)}',
                        (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, (0, 255, 0), 2)
    except:
        pass

    #me.send_rc_control(0, 0, 0, 0)

    cv2.imshow("Image", img)
    cv2.waitKey(1)