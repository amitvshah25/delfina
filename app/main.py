import requests
import os
from typing import Union
from fastapi import FastAPI, Request
from starlette.responses import StreamingResponse
from PIL import Image
from io import BytesIO
from requests.exceptions import HTTPError
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
async def dead_root():
    return {"delfina": "Random Dolphin Images"}

@app.get("/picture")
@limiter.limit("1/second")
async def picture(request: Request):
    return StreamingResponse(unsplash(), media_type="image/jpg")

def unsplash():
    image_url_response = requests.get(os.environ['UNSPLASH_API_URL'] + "&client_id=" + os.environ['UNSPLASH_CLIENT_ID'])
    image_url_response.raise_for_status()
    image_data_response = requests.get(image_url_response.json()['urls']['small'])
    image_data_response.raise_for_status()
    return BytesIO(image_data_response.content)
