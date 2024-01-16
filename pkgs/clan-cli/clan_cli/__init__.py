# Imports
import argparse
import logging
import sys
from types import ModuleType
from typing import Optional

# Custom imports
from . import webui
from .custom_logger import setup_logging

# Setting up the logger
log = logging.getLogger(__name__)

# Trying to import argcomplete module, if not present, set it to None
argcomplete: Optional[ModuleType] = None
try:
    import argcomplete  # type: ignore[no-redef]
except ImportError:
    pass


# Function to create the main argument parser
def create_parser(prog: Optional[str] = None) -> argparse.ArgumentParser:
    # Creating the main argument parser with a description
    parser = argparse.ArgumentParser(prog=prog, description="cLAN tool")

    # Adding a debug argument to enable debug logging
    parser.add_argument(
        "--debug",
        help="Enable debug logging",
        action="store_true",
    )

    # Adding subparsers for different commands
    subparsers = parser.add_subparsers()

    # Adding a subparser for the "webui" command
    parser_webui = subparsers.add_parser("webui", help="start webui")
    # Registering additional arguments for the "webui" command
    webui.register_parser(parser_webui)

    # Using argcomplete for shell autocompletion if available
    if argcomplete:
        argcomplete.autocomplete(parser)

    # If no command-line arguments provided, print the help message
    if len(sys.argv) == 1:
        parser.print_help()
    return parser


# this will be the entrypoint under /bin/clan (see pyproject.toml config)
### Main entry point function
def main() -> None:
    # Creating the main argument parser
    parser = create_parser()
    # Parsing command-line arguments
    args = parser.parse_args()

    # Setting up logging based on the debug flag
    if args.debug:
        setup_logging(logging.DEBUG)
        log.debug("Debug log activated")
    else:
        setup_logging(logging.INFO)

    # If the parsed arguments do not have the "func" attribute, exit
    if not hasattr(args, "func"):
        return

    # Calling the function associated with the specified command
    args.func(args)


# Entry point for script execution
if __name__ == "__main__":
    main()
