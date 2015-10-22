import unittest
import sys
import os
import numpy as np
import logging

from mock import Mock
import cv2


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from api.capture2 import PointsCapture, ImageCapture
from helpers import FakeCamera


# class PointCaptureTest(unittest.TestCase):
#     def 


class ImageCaptureTest(unittest.TestCase):
    def show_it(self, image):
        print(image)
        while True:
            cv2.imshow('frame', image)
            key = chr(cv2.waitKey(1) & 0xFF)
            if key == 'q':
                break

    def test_handle_given_a_frame_should_store_the_right_edge(self):
        sections = 200
        frame = np.ones((100, 130, 3), dtype='uint8') * 128
        frame[:, -1] = (255, 0, 0)
        expected = np.zeros((100, sections, 3), dtype='uint8')
        expected[:, 0] = (255, 0, 0)
        image_capture = ImageCapture(sections)
        image_capture.handle(frame)

        self.assertTrue((image_capture.image[0] == expected[0]).all())

    def test_handle_should_store_the_slice_at_the_given_index(self):
        sections = 200
        frame = np.ones((100, 130, 3), dtype='uint8') * 128
        frame[:, -1] = (255, 0, 0)
        expected = np.zeros((100, sections, 3), dtype='uint8')
        expected[:, 20] = (255, 0, 0)
        image_capture = ImageCapture(sections)
        image_capture.handle(frame, 20)

        self.assertTrue((image_capture.image == expected).all())

    def test_handle_should_return_expected_image_when_called_multiple_times(self):
        sections = 200
        frame = np.ones((100, 130, 3), dtype='uint8') * 128
        frame2 = frame.copy()
        frame[:, -1] = (255, 0, 0)
        frame2[:, -1] = (0, 0, 255)
        expected = np.zeros((100, sections, 3), dtype='uint8')
        expected[:, 0] = (255, 0, 0)
        expected[:, 1] = (0, 0, 255)
        image_capture = ImageCapture(sections)

        image_capture.handle(frame, 0)
        image_capture.handle(frame2, 1)

        self.assertTrue((image_capture.image == expected).all())

    def test_camera_displays_image(self):
        camera = FakeCamera()
        while True:
            cv2.imshow('frame', camera.read())
            key = chr(cv2.waitKey(1) & 0xFF)
            if key == 'q':
                break

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level='INFO')
    unittest.main()