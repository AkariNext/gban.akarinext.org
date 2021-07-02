from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi_versioning import versioned_api_route
from pydantic import BaseModel

from app import app

router = APIRouter(route_class=versioned_api_route(1))


class BanInfo(BaseModel):
    reporter: str
    reason: str
    server_id: str
    banned_username: str


@app.post('/ban/')
async def index(ban_info:BanInfo):
    return JSONResponse({"test": "test"})
