import cv2
import imutils

import time
import numpy as np

try: 
    from imutils.video.pivideostream import PiVideoStream
except ModuleNotFoundError:
    usePiCamera = False
    from imutils.video.webcamvideostream import WebcamVideoStream


class VideoStream:
    def __init__(self, src=0, resolution=(320, 240), framerate=32):
        # check to see if the picamera module should be used
        if usePiCamera:
            self.stream = PiVideoStream(resolution=resolution,
            framerate=framerate)
        # otherwise, we are using OpenCV so initialize the webcam
        # stream
        else:
            self.stream = WebcamVideoStream(src=src)
        
        time.sleep(3)  # Let the sensor warm-up
        self.stream.start()
            

    def start(self):
        # start the threaded video stream
        return self.stream.start()

    def update(self):
        # grab the next frame from the stream
        self.stream.update()

    def read(self):
        # return the current frame
        image = self.stream.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def stop(self):
        # stop the thread and release any resources
        self.stream.stop()
