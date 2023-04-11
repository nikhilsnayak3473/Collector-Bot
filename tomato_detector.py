import numpy as np
import cv2


class TomatoDetector:
    def __init__(self, color):
        self.focal_length = 450
        self.width_of_object = 4
        self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        self.lower_color, self.upper_color = self.get_color_range(color)
        self.min_contour_area = 1000
        self.max_contour_area = 100000

    def get_color_range(self, color):
        colors = {
            "RED": (np.array([0, 100, 100]), np.array([10, 255, 255])),
            "YELLOW": (np.array([20, 100, 100]), np.array([30, 255, 255]))
        }
        return colors.get(color.upper())

    def get_distance(self, img):
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_img, self.lower_color, self.upper_color)
        morph_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel, iterations=5)
        contours, _ = cv2.findContours(morph_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            cnts = [c for c in contours if self.min_contour_area < cv2.contourArea(c) < self.max_contour_area]
            if cnts:
                cnt = max(cnts, key=cv2.contourArea)
                rect = cv2.minAreaRect(cnt)
                pixels = rect[1][0]
                distance = (self.width_of_object * self.focal_length) / pixels
                return distance

        return None

