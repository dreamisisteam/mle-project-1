import io
import os

import pytest


class TestDetection:
    @pytest.fixture(autouse=True)
    def setup(self, model):
        self.model = model
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), './images/test.png'), 'rb') as image_string:
            io_file = io.BytesIO(image_string.read())
        _, self.logs = model.predict(io_file)

    def test_classes(self):
        assert 'dog' in self.logs['class_names']
        assert 'sandwich' in self.logs['class_names']
        assert 'person' in self.logs['class_names']

    def test_speed(self):
        time_ms = 0
        for key in self.logs['speed']:
            time_ms += self.logs['speed'][key]
        assert time_ms < 1000
