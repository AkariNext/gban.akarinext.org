import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_discord import DiscordOAuthClient
from fastapi_versioning import VersionedFastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

db_user = os.environ.get('DATABASE_USER')
db_port = os.environ.get('DATABASE_PORT')
db_host = os.environ.get('DATABASE_HOST')
db_password = os.environ.get('DATABASE_PASSWORD')
db_default_database = os.environ.get('DATABASE_DATABASE')

discord_client = os.environ.get('DISCORD_CLIENT')
discord_client_secret = os.environ.get('DISCORD_CLIENT_SECRET')
discord_redirect_url = os.environ.get('DISCORD_REDIRECT_URL')

app = FastAPI()
discord = DiscordOAuthClient(f'{discord_client}', f'{discord_client_secret}', f'{discord_redirect_url}', ('identify', 'guilds', 'email'))  # scopes
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_default_database}', echo=False)  # DEBUG時はTrueに

Session = sessionmaker(bind=engine, autoflush=True)
session = Session()

Base = declarative_base()
from app.router.v1.auth import index as auth
from app.router.v1.ban import index as ban

app.include_router(auth.router)
app.include_router(ban.router)
app = VersionedFastAPI(app, version_format='{major}', prefix_format='/v{major}')
