# nav_handler.py
# Written by: Will Plachno
# Created: 12/15/2025
# Version: 0.0.1.001
# Last Changed: 12/16/2025

from pathlib import Path
from typing import Optional

from utilities.wcmodehandler import WoodchipperCoreModeHandler
from navigation.core.nav_bookmark import Bookmark
from navigation.core.nav_list import BookmarkList
from navigation.constants import RESULTS, ERROR

class BookmarkHandler(WoodchipperCoreModeHandler):
    def __init__(self, request, response):
        WoodchipperCoreModeHandler.__init__(self, request, response)

        self.mode:   str                = self.request.mode
        self.label:  Optional[str]      = self.request.label
        self.path:   Optional[Path]     = self.request.path

        self.list:   BookmarkList       = BookmarkList()

        self.log_kvp(RESULTS.CHANGELIST, [])

        self.target: Optional[Bookmark] = None
        self.source: Optional[Bookmark] = None

        if self.label:
            self.source = self.list.find(self.label)

            target_path:Optional[Bookmark.PathSource] = self.path
            if not target_path:
                target_path = self.request.cwd
            self.target = Bookmark(self.label, target_path)

    def add_entry(self, status:str, bookmark_or_label:BookmarkList.LabelSource) -> None:
        entry:RESULTS.ChangelistEntry
        if type(bookmark_or_label) == str:
            entry = status, bookmark_or_label, RESULTS.STATUS.MISSING
        else:
            entry = status, bookmark_or_label.get_label(), str(bookmark_or_label.get_path())
        self.results.changelist.append(entry)

    def compile_success(self, save:bool=True, success:bool=True):
        if success:
            self.log_success()
            if save:
                try:
                    self.list.save()
                except Exception as e:
                    self.log_error(str(e))


class BookmarkAddHandler(BookmarkHandler):
    def handle(self):
        if self.source:
            self.log_error(ERROR.ADD_EXISTING_BOOKMARK.format(self.label))
        else:
            self.list.add(self.target)
            self.add_entry(RESULTS.STATUS.ADDED, self.target)
            self.compile_success()


class BookmarkSetHandler(BookmarkHandler):
    def handle(self):
        if not self.source:
            self.log_error(ERROR.SET_MISSING_BOOKMARK.format(self.label))
        else:
            bookmarks:BookmarkList.BookmarkChange = self.list.set(self.target)
            self.add_entry(RESULTS.STATUS.FOUND, bookmarks[0])
            self.add_entry(RESULTS.STATUS.UPDATED, bookmarks[1])
            self.compile_success()


class BookmarkRemoveHandler(BookmarkHandler):
    def handle(self):
        if not self.source:
            self.add_entry(RESULTS.STATUS.MISSING, self.target)
            self.compile_success(save=False)
        else:
            self.list.remove(self.source)
            self.add_entry(RESULTS.STATUS.REMOVED, self.source)
            self.compile_success()


class BookmarkShowHandler(BookmarkHandler):
    def __init__(self, request, response):
        super().__init__(request, response)
        self.log_kvp(RESULTS.SHOW.KEY, RESULTS.SHOW.ONE if self.target else RESULTS.SHOW.ALL)

    def handle(self):
        if self.source:
            self.add_entry(RESULTS.STATUS.FOUND, self.source)
            self.compile_success(save=False)
        elif self.target:
            self.add_entry(RESULTS.STATUS.MISSING, self.target)
            self.compile_success(save=False)
        else:
            for bookmark in self.list.get_list():
                self.add_entry(RESULTS.STATUS.FOUND, bookmark)
            self.compile_success(save=False)

class BookmarkExportHandler(BookmarkHandler):
    def __init__(self, request, response):
        super().__init__(request, response)
        self.log_kvp(RESULTS.PORT.KEY, self.mode)
        self.log_kvp(RESULTS.PORT.FILE, str(self.path))
        self.target_file = BookmarkList(self.path)
        self.source = self.list
        self.destination = self.target_file

    def handle(self):
        self.destination.set_list(self.source.get_list())
        self.destination.save()
        self.log_success()

class BookmarkImportHandler(BookmarkExportHandler):
    def __init__(self, request, response):
        super().__init__(request, response)
        self.source = self.target_file
        self.destination = self.list