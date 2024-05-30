from ultralytics import YOLO


class ObjectDetection:
    """on init"""

    def __init__(self, weights: str) -> None:
        self.model = YOLO(weights)

    def predict(self):
        pass
