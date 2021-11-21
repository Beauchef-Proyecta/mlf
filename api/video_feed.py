import cv2
import os
import sys
import time

sys.path.insert(0, os.path.abspath('..'))
from mlf.core.camera import VideoStream

class VideoFeed():

    def __init__(self):
        self.video_stream = VideoStream(src=2)

    def gen(self):
        """ Generator function (see more about `yield` documentation)
        """
        while True:
            frame = self.video_stream.read()
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
    
    def grab_single_frame(self):
        frame = self.video_stream.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

