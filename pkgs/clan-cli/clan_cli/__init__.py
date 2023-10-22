import argparse
import logging
import sys
from types import ModuleType
from typing import Optional

from . import webui
from .custom_logger import register

log = logging.getLogger(__name__)

argcomplete: Optional[ModuleType] = None
try:
    import argcomplete  # type: ignore[no-redef]
except ImportError:
    pass


def create_parser(prog: Optional[str] = None) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=prog, description="cLAN tool")

    parser.add_argument(
        "--debug",
        help="Enable debug logging",
        action="store_true",
    )

    subparsers = parser.add_subparsers()

    parser_webui = subparsers.add_parser("webui", help="start webui")
    webui.register_parser(parser_webui)

    #    if args.debug:
    register(logging.DEBUG)
    log.debug("Debug log activated")

    if argcomplete:
        argcomplete.autocomplete(parser)

    if len(sys.argv) == 1:
        parser.print_help()
    return parser


# this will be the entrypoint under /bin/clan (see pyproject.toml config)
def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if not hasattr(args, "func"):
        return

    args.func(args)


if __name__ == "__main__":
    main()
