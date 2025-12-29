# nav.py
# Written by: Will Plachno
# Created:12/15/25
# Version: 0.0.1.001
# Last Changed: 12/17/2025

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utilities.wccore import WoodchipperCore as WCCore
from navigation.constants import MODE

import navigation.interface.nav_parser as parser
import navigation.core.nav_handler as handlers
import navigation.interface.nav_printer as printers

def _main(args):
    core = WCCore()
    core.set_parser_builder(parser.build_parser)
    core.set_post_parser(parser.post_parser)
    core.add_mode(
        MODE.SHOW,
        handlers.BookmarkShowHandler,
        printers.BookmarkShowPrinter)
    core.add_mode(
        MODE.ADD,
        handlers.BookmarkAddHandler,
        printers.BookmarkPrinter)
    core.add_mode(
        MODE.SET,
        handlers.BookmarkSetHandler,
        printers.BookmarkPrinter)
    core.add_mode(
        MODE.REMOVE,
        handlers.BookmarkRemoveHandler,
        printers.BookmarkPrinter)
    core.add_mode(
        MODE.EXPORT,
        handlers.BookmarkExportHandler,
        printers.BookmarkPortPrinter)
    core.add_mode(
        MODE.IMPORT,
        handlers.BookmarkImportHandler,
        printers.BookmarkPortPrinter)
    core.run()

if __name__ == "__main__":
    _main(sys.argv)
