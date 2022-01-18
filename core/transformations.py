import numpy as np


def rotation_around_x(vector, angle):
    R = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle), -np.sin(angle), 0],
        [0, np.sin(angle), np.cos(angle), 0],
        [0, 0, 0, 1],
    ])
    return np.matmul(R, vector)


def rotation_around_z(vector, angle):
    R = np.array([
        [np.cos(angle), -np.sin(angle), 0, 0],
        [np.sin(angle), np.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    return np.matmul(R, vector)


def rotation_around_y(vector, angle):
    R = np.array([
        [np.cos(angle), 0, np.sin(angle), 0],
        [0, 1, 0, 0],
        [-np.sin(angle), 0, np.cos(angle), 0],
        [0, 0, 0, 1],
    ])
    return np.matmul(R, vector)


def translation_along_x(vector, distance):
    T = np.array([[1, 0, 0, distance], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    return np.matmul(T, vector)


def translation_along_y(vector, distance):
    T = np.array([[1, 0, 0, 0], [0, 1, 0, distance], [0, 0, 1, 0], [0, 0, 0, 1]])
    return np.matmul(T, vector)


def translation_along_z(vector, distance):
    T = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, distance], [0, 0, 0, 1]])
    return np.matmul(T, vector)
