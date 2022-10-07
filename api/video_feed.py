import cv2
import time

from core.vision.camera import VideoStream


class VideoFeed:
    def __init__(self):
        self.video_stream = VideoStream()

    def gen(self):
        """Generator function (see more about `yield` documentation)"""
        while True:
            frame = self.video_stream.read()
            ret, jpeg = cv2.imencode(".jpg", frame)
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n\r\n"
            )

    def grab_single_frame(self):
        frame = self.video_stream.read()
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()
