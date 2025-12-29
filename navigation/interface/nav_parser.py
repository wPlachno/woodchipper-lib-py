# nav_parser.py
# Written by: Will Plachno
# Created: 12/15/2025
# Version: 0.0.1.001
# Last Changed: 12/15/2025

from os import getcwd
from pathlib import Path
from utilities.wcparser import CLParser as WCParser
from navigation.constants import MODE, META, ARGS

def build_parser() -> WCParser:
    parser: WCParser = WCParser(
        META.NAME,
        version=META.VERSION,
        description=META.DESCRIPTION,
        footer=META.FOOTER)
    parser.add_argument(
        ARGS.MODE.NAME,
        choices=[MODE.SHOW, MODE.ADD, MODE.SET, MODE.REMOVE],
        default=MODE.SHOW,
        description=ARGS.MODE.DESCRIPTION)
    parser.add_argument(
        ARGS.LABEL.NAME,
        description=ARGS.LABEL.DESCRIPTION)
    parser.add_argument(
        ARGS.PATH.NAME,
        shaper=path_shaper,
        description=ARGS.PATH.DESCRIPTION)
    return parser

def post_parser(raw_request:any) -> any:
    request = raw_request
    setattr(request, "cwd", Path(getcwd()))
    return request

def path_shaper(text: str) -> Path:
    return Path(text).resolve()