import numpy as np
import cv2


class TomatoDetector:
    def __init__(self, color):
        self.focal = 450
        self.width = 4
        self.kernel = np.ones((3, 3), 'uint8')
        self.lower, self.upper = self.get_upper_lower(color)

    def get_upper_lower(self, color):
        if color == 'RED':
            return (np.array([0, 50, 120]), np.array([10, 255, 255]))
        elif color == 'YELLOW':
            return (np.array([20, 190, 20]), np.array([30, 255, 255]))

    def get_distance(self, img):
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_img, self.lower, self.upper)
        d_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                                 self.kernel, iterations=5)
        contours, _ = cv2.findContours(
            d_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
        for cnt in contours:
            if(cv2.contourArea(cnt) > 100 and cv2.contourArea(cnt) < 306000):
                rect = cv2.minAreaRect(cnt)
                pixels = rect[1][0]
                distance = (self.width*self.focal)/pixels
                return distance
