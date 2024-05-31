from model_detection import ObjectDetection
import pytest

model = ObjectDetection()


@pytest.fixture(scope='session', name='model')
def model_fixture():
    return model
