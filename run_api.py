import uvicorn
import argparse


RUN_API = "api.main:api"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_DEV_PORT = 8000
DEFAULT_PROD_PORT = 8443


parser = argparse.ArgumentParser(
    prog = 'run_api.py',
    description = 'Runs the Fast API for different environments',
    epilog=f'Default behavior with no options provided will run in development mode on port {DEFAULT_DEV_PORT}'
)
parser.add_argument('--port', help=f'port number to use', type=int, dest="port")
parser.add_argument('--host', help=f'host address to use', type=str, dest="host", default=DEFAULT_HOST)
parser.add_argument('--prod', help='runs api in production mode (DEFAULT: dev)', action='store_true', dest="production")


def run_dev(use_host, use_port):
    if use_port == None:
        use_port = DEFAULT_DEV_PORT
    uvicorn.run(RUN_API, host=use_host, port=use_port, reload=True, log_level="debug")


def run_prod(use_host, use_port):
    if use_port == None:
        use_port = DEFAULT_PROD_PORT
    uvicorn.run(RUN_API, host=use_host, port=use_port)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.production:
        run_prod(args.host, args.port)
    else:
        run_dev(args.host, args.port)