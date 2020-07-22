import os
from fastapi import FastAPI
from fastapi import Path
from fastapi.responses import RedirectResponse
from http import HTTPStatus
import json
from pydantic import BaseModel

import config
import utils


app = FastAPI(
    title="app",
    description="",
    version="1.0.0",
)


@utils.construct_response
@app.get("/")
async def _index():
    response = {
        'message': HTTPStatus.OK.phrase,
        'status-code': HTTPStatus.OK,
        'data': {}
    }
    config.logger.info(json.dumps(response, indent=2))
    return response


class PredictPayload(BaseModel):
    pass


@utils.construct_response
@app.post("/predict")
async def _predict(payload: PredictPayload):
    pass
