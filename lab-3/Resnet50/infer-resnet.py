#!/usr/bin/python3

import cv2
import subprocess
import time
import sys

def detect_from_camera():
    print ('Inside loop of detect from camera')
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    while (cap.isOpened()):
    	success, image = cap.read()
        cv2.imwrite('/home/root/DRPAI-test/app_resnet50_img/src/sample.bmp', image)
    	start=time.time()
    	results = subprocess.run(args = './sample_app_resnet50_img', capture_output = True, shell= True, universal_newlines=True)
    	stop = time.time()
    	print (results.stdout)
    	print(f'time for inference is {stop-start:.2f} seconds')
    cap.release()

if __name__ == '__main__':
    detect_from_camera()
