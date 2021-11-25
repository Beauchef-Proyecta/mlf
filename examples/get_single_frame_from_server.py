import cv2
import numpy as np
import os
import sys
import time

sys.path.insert(0, os.path.abspath('..'))

from mlf.api.client import ClientWrapper


c = ClientWrapper()
img = c.get_single_frame()
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()