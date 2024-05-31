import pytest

from model_detection import ObjectDetection

model = ObjectDetection()


@pytest.fixture(scope="session", name="model")
def model_fixture():
    return model
