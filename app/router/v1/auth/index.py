from fastapi import APIRouter, Request
from fastapi_discord import Unauthorized
from fastapi_versioning import versioned_api_route
from fastapi.responses import RedirectResponse

from app import discord

router = APIRouter(route_class=versioned_api_route(1))


@router.get("/login")
async def login():
    return RedirectResponse(discord.oauth_login_url)


@router.get("/callback")
async def callback(code: str):
    token, refresh_token = await discord.get_access_token(code)
    return RedirectResponse(f'https://gban.akarinext.org/login?token={token}&refresh_token={refresh_token}')


@router.get("/profile")
@discord.requires_authorization
async def hello(request: Request):
    return await discord.user(request)


@router.get('/authenticated')
async def auth(request: Request):
    try:
        token = discord.get_token(request)
        auth = await discord.isAuthenticated(token)
        return f'{auth}'
    except Unauthorized:
        return 'False'
