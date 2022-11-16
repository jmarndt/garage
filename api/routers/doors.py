from fastapi import APIRouter, HTTPException, status
from gpiozero import OutputDevice
from time import sleep
from ..garage import garage_doors


router = APIRouter(prefix="/doors")


@router.get("")
def get_doors():
    return get_doors()


@router.get("/{door_id}")
def get_door(door_id: int):
    try:
        return get_door(door_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/{door_id}")
def toggle_door(door_id: int):
    try:
        door =  get_door(door_id)
        gpio_high(door.control_pin)
        return door
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


def get_doors():
    return garage_doors


def get_door(door_id: int):
    result = [filter(lambda x: x.door_id == door_id, garage_doors)]
    if len(result) != 1: raise ValueError
    return result.pop()


def gpio_high(pin: int):
    gpio = OutputDevice(pin)
    gpio.on()
    sleep(0.3)
    gpio.off()
    sleep(1)