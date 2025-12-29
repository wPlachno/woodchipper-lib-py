# wcgig_parser.py
# Created: 12/26/24
# Version: 0.0.1.002
# Last Changes: 12/29/2025

import pathlib

from utilities.wcparser import CLParser as WCParser
from gignore.constants import META, ARGS, MODE

def build_parser():
    parser = WCParser(META.NAME,
                      version=META.VERSION,
                      description=META.DESCRIPTION,
                      footer=META.FOOTER)
    parser.add_argument(ARGS.MODE.NAME, choices=[MODE.SHOW, MODE.ADD, MODE.SETUP, MODE.REMOVE, MODE.CLEAR], default=MODE.SHOW,
                        description=ARGS.MODE.DESCRIPTION)
    parser.add_argument(ARGS.TARGET.NAME, nargs="+",
                        description=ARGS.TARGET.DESCRIPTION)
    return parser

def path_shaper(text):
    return pathlib.Path(text).resolve()
