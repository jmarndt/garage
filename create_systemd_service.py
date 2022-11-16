import os
import venv


RUN_PATH = os.path.dirname(os.path.realpath(__file__))
API_NAME = RUN_PATH.split('/')[-1]
PY_ENV_PATH = f'{RUN_PATH}/env'
SERVICE_PATH = "/etc/systemd/system"
SERVICE_FILE = f"""[Unit]
Description = {API_NAME.capitalize()} service
After = network.target

[Service]
Type = simple
Restart = always
SyslogIdentifier = {API_NAME.capitalize()}
ExecStart = {PY_ENV_PATH}/bin/python {RUN_PATH}/run_api.py --prod

[Install]
WantedBy = multi-user.target"""


def build_python_env():
    venv.create(PY_ENV_PATH, with_pip=True)
    os.system(f'{PY_ENV_PATH}/bin/python -m pip install -r requirements.txt')


def create_service_file():
    with open(f"{SERVICE_PATH}/{API_NAME}.service", "w") as file:
            file.write(SERVICE_FILE)


def enable_service():
    os.system(f'systemctl enable {API_NAME}')
    os.system('systemctl daemon-reload')
    os.system(f'systemctl start {API_NAME}')


if __name__ == '__main__':
    build_python_env()
    create_service_file()
    enable_service()
