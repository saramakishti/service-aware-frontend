import argparse
import logging
from typing import Callable, NoReturn, Optional

# Get the logger for this module
log = logging.getLogger(__name__)

# Initialize variables for server startup and potential ImportError
start_server: Optional[Callable] = None
ServerImportError: Optional[ImportError] = None

# Try importing the start_server function from the server module
try:
    from .server import start_server
except ImportError as e:
    # If ImportError occurs, log the exception and store it in ServerImportError
    log.exception(e)
    ServerImportError = e


# Function to be called when FastAPI is not installed
##########################################################################################
# usage: clan webui [-h] [--port PORT] [--host HOST] [--populate] [--emulate] [--no-open] [--dev]
#                  [--dev-port DEV_PORT] [--dev-host DEV_HOST] [--reload]
#                  [--log-level {critical,error,warning,info,debug,trace}]
#                  [sub_url]
#
# positional arguments:
#  sub_url               Sub URL to open in the browser
#
# options:
#  -h, --help            show this help message and exit
#  --port PORT           Port to listen on
#  --host HOST           Host to listen on
#  --populate            Populate the database with dummy data
#  --emulate             Emulate two entities c1 and c2 + dlg and ap
#  --no-open             Don't open the browser
#  --dev                 Run in development mode
#  --dev-port DEV_PORT   Port to listen on for the dev server
#  --dev-host DEV_HOST   Host to listen on
#  --reload              Don't reload on changes
#  --log-level {critical,error,warning,info,debug,trace}
#                        Log level
##########################################################################################
def fastapi_is_not_installed(_: argparse.Namespace) -> NoReturn:
    assert ServerImportError is not None
    print(
        f"Dependencies for the webserver are not installed. The webui command has been disabled ({ServerImportError})"
    )
    exit(1)


# Function to register command-line arguments for the webserver
def register_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--port", type=int, default=2979, help="Port to listen on")
    parser.add_argument(
        "--host", type=str, default="localhost", help="Host to listen on"
    )
    parser.add_argument(
        "--populate",
        action="store_true",
        help="Populate the database with dummy data",
        default=False,
    )
    parser.add_argument(
        "--emulate",
        action="store_true",
        help="Emulate two entities c1 and c2 + dlg and ap",
        default=False,
    )
    parser.add_argument(
        "--no-open", action="store_true", help="Don't open the browser", default=False
    )
    parser.add_argument(
        "--dev", action="store_true", help="Run in development mode", default=False
    )
    parser.add_argument(
        "--dev-port",
        type=int,
        default=3000,
        help="Port to listen on for the dev server",
    )
    parser.add_argument(
        "--dev-host", type=str, default="localhost", help="Host to listen on"
    )
    parser.add_argument(
        "--reload", action="store_true", help="Don't reload on changes", default=False
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="info",
        help="Log level",
        choices=["critical", "error", "warning", "info", "debug", "trace"],
    )

    parser.add_argument(
        "sub_url",
        type=str,
        default="/",
        nargs="?",
        help="Sub URL to open in the browser",
    )

    # Set the args.func variable in args based on whether FastAPI is installed
    if start_server is None:
        parser.set_defaults(func=fastapi_is_not_installed)
    else:
        parser.set_defaults(func=start_server)
