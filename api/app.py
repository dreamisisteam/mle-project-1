from io import BytesIO
from typing import Annotated
from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, Form, Request, Response
from fastapi.exceptions import HTTPException

try:
    # import from source
    from model_detection.model_detection import model
except ImportError:
    # import from library
    from model_detection import model


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Activate preparation of used models"""
    # TODO: add support of env configuring
    # default path to pretrained weights
    setattr(app, 'object_detection_model', model.ObjectDetection())
    yield

app = FastAPI(lifespan=lifespan)


class HealthCheckModel(BaseModel):
    status: bool = None


@app.get('/api/v1/health', response_model=HealthCheckModel)
def healthcheck():
    """ Healthcheck """
    return {'status': True}


@app.post('/api/v1/detect/', responses={200: {'content': {'image/jpeg': {}}}})
async def detect(
        request: Request,
        file: Annotated[UploadFile, File()],
        confidence: Annotated[float, Form()] = 0.5,
):
    """ Endpoint of detection """
    if "image/" not in file.content_type:
        raise HTTPException(
            status_code=400,
            detail={"file": "Should be an image!"}
        )

    image_io = BytesIO(await file.read())
    result_img: BytesIO = request.app.object_detection_model.predict(
        image_io, confidence=confidence)[0]

    return Response(content=result_img.read(), media_type='image/jpeg')
