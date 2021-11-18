import cv2
import os
import sys
import time

sys.path.insert(0, os.path.abspath('..'))
from mlf.core.camera import VideoStream

class VideoFeed():

    def __init__(self):
        self.video_stream = VideoStream(src=1)

    def gen(self):
        while True:
            frame = self.video_stream.read()
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
