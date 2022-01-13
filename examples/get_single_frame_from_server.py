import cv2
import numpy as np
import os
import sys
import time

sys.path.insert(0, os.path.abspath('..'))

from mlf.api.client import ClientWrapper


c = ClientWrapper() # Si no se especifica url, pide al 'localhost' (misma raspi)
img = c.get_single_frame()

# Si esta corriendo en una raspberry, las siguientes lineas arrojan error
# porque las raspis no tienen instalados los drives para desplegar graficos
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
