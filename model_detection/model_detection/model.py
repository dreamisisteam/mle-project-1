import io
import os
from typing import Optional, Union

from PIL import Image
from ultralytics import YOLO


class ObjectDetection:
    """Class for Object Detection"""

    def __init__(
        self,
        weights: str = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "./models/yolov8x.pt"
        ),
    ) -> None:
        """Weights loading takes time. Better init model before usage and once"""
        self.model = YOLO(weights)

    def predict(
        self,
        image_bin: io.BytesIO,
        confidence: float = 0.5,
        log_info: bool = True,
    ) -> Union[io.BytesIO, Optional[dict]]:
        """Method for getting predicted img

        Args:
            image_bin (`io.BytesIO`): image in `io.BytesIO` data type
            confidence (`float`, optional): threshold probability. Defaults to `0.5`.
            log_info (`bool`, optional): if `True`, returned logs. Defaults to `True`.

        Returns:
            Union[io.BytesIO, Optional[dict]]: image in bytes & None or logs
        """  # noqa: E501
        img = Image.open(image_bin)
        result_images = self.model(source=img, conf=confidence)[0]

        result_byte_io = io.BytesIO()
        result_pil_image = Image.fromarray(result_images.plot()[..., ::-1])
        result_pil_image.save(result_byte_io, format="JPEG")
        result_byte_io.seek(0)

        if log_info:
            speed = result_images.speed
            classes = result_images.boxes.cls.cpu().numpy().tolist()
            confs = result_images.boxes.conf.cpu().numpy().tolist()
            class_names = [
                result_images.names[key]
                for key in classes
                if key in result_images.names
            ]

            logs = {
                "speed": speed,
                "classes": classes,
                "class_names": class_names,
                "confs": confs,
            }
            return result_byte_io, logs

        return result_byte_io, None
