import numpy as np

from .transformations import (
                        rotation_around_x, 
                        rotation_around_y, 
                        rotation_around_z,
                        translation_along_x )


class Link:

    rotation_map = {'x': rotation_around_x,
                    'y': rotation_around_y,
                    'z': rotation_around_z,}

    def __init__(self, length: float, rotation=None,  parent=None):
        self.parent = parent
        self._length = length
        self._rotation = rotation if rotation else {'x': 0, 'y': 0, 'z': 0}
        self.origin_matrix = np.identity(4)
        self.end_matrix = np.identity(4)

        if parent:
            self.set_origin(parent.end_matrix)
        
        self.set_pose(self._rotation)
        

    @property
    def start_coordinates(self):
        m = self.origin_matrix
        return (m[0][3], m[1][3], m[2][3])
    
    @property
    def end_coordinates(self):
        m = self.end_matrix
        return (m[0][3], m[1][3], m[2][3])

    def set_origin(self, matrix):
        self.origin_matrix = matrix
    
    def set_pose(self, rotation):
        self.end_matrix = self.origin_matrix.copy()
        self._rotate(rotation)
        self.end_matrix = np.dot(self.end_matrix, translation_along_x(self._length))

    def _rotate(self, rotation: dict):
        for axis, value in rotation.items():
            if value:
                R = rotation_map[axis](angle)
                self.end_matrix = R * self.end_matrix
                self._rotation[axis] = value


