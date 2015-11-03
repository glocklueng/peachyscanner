import numpy as np

from infrastructure.point_converter import PointConverter

class ImageCapture(object):

    def __init__(self, sections):
        self.sections = sections
        self._section_count = 0
        self.image = None

    def handle(self, frame=None, section=0):
        self._section_count += 1
        self._image(frame.shape[0])[:, section] = frame[:, -1]
        return self._section_count < self.sections

    def _image(self, y_axis_dimension):
        if self.image is None:
            self.image = np.zeros((y_axis_dimension, self.sections, 3), dtype='uint8')
        return self.image


class PointCapture(object):

    def __init__(self, sections):
        self.sections = sections
        self.points = None

    def handle(self, **kwargs): 
        self._points(kwargs['detected'].shape[0])
        return 0

    def _points(self, height):
        if self.points is None:
            self.points = np.zeros((height, self.sections), dtype='int32')
        else:
            self.points

    def get_points(self, frame):
        # maxindex = np.argmax(frame, axis=1)
        # data = (np.ones(maxindex.shape[0]) * maxindex.shape[0]) - maxindex
        # data[data < 0] = 0
        # data[data == maxindex.shape[0]] = 0
        return 0
