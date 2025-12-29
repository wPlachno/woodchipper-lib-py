# wcn_parser.py
# Written by: Will Plachno
# Created: 01/04/2025
# Version: 0.0.1.004
# Last Changed: 12/29/2025

from utilities.wcparser import CLParser as WCParser
from notes.constants import MODE, SECTION, META, ARGS

def build_parser():
    parser = WCParser(META.NAME,
                      version=META.VERSION,
                      description=META.DESCRIPTION,
                      footer=META.FOOTER)
    parser.add_argument(ARGS.MODE.NAME, choices=[MODE.SHOW, MODE.ADD, MODE.REMOVE, MODE.MOVE, MODE.UPDATE, MODE.REPLACE, MODE.CLEAR], default=MODE.DEFAULT,
                        description=ARGS.MODE.DESCRIPTION)
    parser.add_argument(ARGS.TARGET.NAME, nargs="+",
                        description=ARGS.TARGET.DESCRIPTION)
    parser.add_argument(ARGS.SECTION.NAME, choices=[SECTION.CORE, SECTION.LOCAL, SECTION.ALL], default=SECTION.ALL,
                        description=ARGS.SECTION.DESCRIPTION)
    return parser

def post_parser(raw_request):
    request = raw_request
    if request.mode == MODE.DEFAULT:
        if len(request.target) == 0:
            request.mode = MODE.SHOW
        else:
            request.mode = MODE.ADD
    setattr(request, "lib", SECTION.TO_LIB[request.section])
    return request