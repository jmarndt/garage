from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from enum import Enum
import json
from gpiozero import OutputDevice
from time import sleep


## API setup
api = FastAPI()
api_keys: dict = {}
garage_doors: list = []

def api_key_auth(api_key: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    if api_key not in api_keys.values():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

class Routes(str, Enum):
    ping = "/garage/ping",
    garage_doors = "/garage/doors"


## Health check
@api.get(Routes.ping)
def ping():
    return {"message": "pong"}


## Garage door controller
class GarageDoor(BaseModel):
    door_id: int
    control_pin: int

@api.get(Routes.garage_doors, dependencies=[Depends(api_key_auth)])
def get_doors():
    return get_doors()

@api.get(Routes.garage_doors + "/{door_id}", dependencies=[Depends(api_key_auth)])
def get_door(door_id: int):
    try:
        return get_door(door_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@api.post(Routes.garage_doors + "/{door_id}", dependencies=[Depends(api_key_auth)])
def toggle_door(door_id: int):
    try:
        door =  get_door(door_id)
        gpio_high(door.control_pin)
        return door
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


## Finalize setup
with open("garage.json", "r") as data:
    config = json.loads(data.read())
    api_keys = config["api_keys"]
    for door_info in config["garage_doors"]:
        garage_doors.append(GarageDoor.parse_raw(json.dumps(door_info)))


## Utility functions
def get_doors() -> list[GarageDoor]:
    return garage_doors

def get_door(door_id: int) -> GarageDoor:
    result = list(filter(lambda x: x.door_id == door_id, garage_doors))
    if len(result) != 1: raise ValueError
    return result.pop()

def gpio_high(pin: int):
    gpio = OutputDevice(pin)
    gpio.on()
    sleep(0.3)
    gpio.off()
    sleep(1)