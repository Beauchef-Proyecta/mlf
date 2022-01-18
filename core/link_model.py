import numpy as np

from .transformations import (
                        rotation_around_x, 
                        rotation_around_y, 
                        rotation_around_z,
                        translation_along_x )


class Link:

    __rotation_functions = {'x': rotation_around_x,
                    'y': rotation_around_y,
                    'z': rotation_around_z,}

    def __init__(self, length: float, axis: str, rotation=None,  parent=None):
        self.parent = parent
        self._length = length
        if axis not in self.__rotation_functions:
            raise ValueError("axis must be equal to 'x', 'y', or 'z'")
        self._axis = axis
        self._rotation = 0
        self._origin = np.array([0,0,0,1])
        self._end = np.array([0,0,0,1])

        if parent:  
            self.set_origin(parent._end)
        self.set_pose(rotation)

    @property
    def origin(self):
        return np.array(self._origin[0:3])
    
    @property
    def end(self):
        return np.array(self._end[0:3])

    def set_origin(self, vector):
        self._origin = vector
    
    def set_pose(self, rotation=None):
        self._end = self._origin.copy()
        self._end = translation_along_x( self._end, self._length)
        if rotation:
            self._rotate(rotation)

    def _rotate(self, angle):
        vector = self._end - self._origin
        rotated = self.__rotation_functions[self._axis](vector, angle)
        self._end = self._origin + rotated
        self._rotation = angle


