# Garage API
An API to control garage doors with a Raspberry Pi and some relays.

---

## Setup
Before running the API a few dependencies need to be installed (FastAPI and Uvicorn). It is recommended to do this in a virtual environment, but doing so is optional.

Create virtual environment (and activate it):
```
python3 -m venv .env && source .env/bin/activate
```

Update pip and install requirements:
```
python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
```

## Running
Simply run the `run_api.py` script to start the API in dev mode:
```
python3 run_api.py
```

To see additional options run it with the help flag:
```
python3 run_api.py -h
```

### As systemd
For systems with systemd, you can create a service to run the API by running the `create_systemd_service.py` script. This script will utilize the `run_api.py` script with the `--prod` flag, so make sure to edit the `run_api.py` default settings to your liking, or edit the `create_systemd_service.py` accordingly.