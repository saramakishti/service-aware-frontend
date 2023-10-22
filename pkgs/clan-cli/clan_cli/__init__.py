import argparse
import logging
import sys
from types import ModuleType
from typing import Optional

from . import config, flakes, join, machines, secrets, vms, webui
from .custom_logger import register
from .ssh import cli as ssh_cli

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

    parser_flake = subparsers.add_parser(
        "flakes", help="create a clan flake inside the current directory"
    )
    flakes.register_parser(parser_flake)

    parser_join = subparsers.add_parser("join", help="join a remote clan")
    join.register_parser(parser_join)

    parser_config = subparsers.add_parser("config", help="set nixos configuration")
    config.register_parser(parser_config)

    parser_ssh = subparsers.add_parser("ssh", help="ssh to a remote machine")
    ssh_cli.register_parser(parser_ssh)

    parser_secrets = subparsers.add_parser("secrets", help="manage secrets")
    secrets.register_parser(parser_secrets)

    parser_machine = subparsers.add_parser(
        "machines", help="Manage machines and their configuration"
    )
    machines.register_parser(parser_machine)

    parser_webui = subparsers.add_parser("webui", help="start webui")
    webui.register_parser(parser_webui)

    parser_vms = subparsers.add_parser("vms", help="manage virtual machines")
    vms.register_parser(parser_vms)

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
