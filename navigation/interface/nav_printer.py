# nav_printer.py
# Written by: Will Plachno
# Created: 12/17/2025
# Version: 0.0.1.001
# Last Changed: 12/29/2025

from navigation.constants import RESULTS, CHANGE, SHOWALL
from utilities.wcconstants import Verbosity, CL_GENERAL
from utilities.wcmodeprinter import WoodchipperCoreModePrinter
from utilities.wcprinter import WoodchipperToolkitPrinter

class BookmarkPrinter(WoodchipperCoreModePrinter):
    def __init__(self, response: any, printer: WoodchipperToolkitPrinter):
        super().__init__(response, printer)
        self.changelist:list[RESULTS.ChangelistEntry] = self.data.changelist

    def print_entry(self, entry:RESULTS.ChangelistEntry) -> None:
        self.printer.pr(CHANGE.FRAME[entry[0]].format(
            entry[1],
            entry[2]
        ))

    def print(self):
        if self.printer.verbosity == Verbosity.RESULTS_ONLY:
            text = CL_GENERAL.SUCCESS if self.data.success else CL_GENERAL.FAILURE
            self.printer.pr(text, Verbosity.RESULTS_ONLY)
        elif self.printer.verbosity >= Verbosity.NORMAL:
            if not self.data.success:
                self.printer.error(self.data.error, new_line=False)
            else:
                for entry in self.changelist:
                    self.print_entry(entry)


class BookmarkShowPrinter(BookmarkPrinter):
    def __init__(self, response: any, printer: WoodchipperToolkitPrinter):
        super().__init__(response, printer)
        self.show = self.data.show

    def print(self):
        if self.printer.verbosity == Verbosity.RESULTS_ONLY and not self.data.success:
            self.printer.pr(CL_GENERAL.FAILURE, Verbosity.RESULTS_ONLY)
        elif self.printer.verbosity >= Verbosity.NORMAL and not self.data.success:
            self.printer.error(self.data.error)
        elif self.printer.verbosity >= Verbosity.RESULTS_ONLY:
            if self.show == RESULTS.SHOW.ALL:
                if len(self.changelist) > 0:
                    for entry in self.changelist:
                        self.printer.pr(SHOWALL.ITEM.format(entry[1], entry[2]), Verbosity.RESULTS_ONLY)
                else:
                    self.printer.pr(SHOWALL.NONE, Verbosity.RESULTS_ONLY)
            else:
                if self.changelist[0][0] == RESULTS.STATUS.FOUND:
                    self.printer.pr(self.changelist[0][2], Verbosity.RESULTS_ONLY)
