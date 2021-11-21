import os
import sys
import requests
import time
import cv2
import numpy as np


class Client:

    def __init__(self, url='http://localhost'):
        self.url = url

    def get_single_frame(self):
        response = requests.get(self.url+':5000/single_frame', stream=True).raw
        image = np.asarray(bytearray(response.read()), dtype="uint8")
        return cv2.imdecode(image, cv2.IMREAD_COLOR)

if __name__ == '__main__':
    c = Client()
    img = c.get_single_frame()
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()