from fastapi import FastAPI, Depends
from .routers import ping, doors
from .dependencies import api_key_auth


api = FastAPI()
api.include_router(ping.router)
api.include_router(doors.router, dependencies=[Depends(api_key_auth)])
