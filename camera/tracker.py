import cv2


class ColorTracker:
    def __init__(self, camera_index: int = 0):
        self.cap = cv2.VideoCapture(camera_index)

    def read_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None
        return frame

    def release(self):
        self.cap.release()
