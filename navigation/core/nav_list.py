# nav_list.py
# Written by: Will Plachno
# Created: 12/15/2025
# Version: 0.0.1.002
# Last Changed: 12/29/2025

from pathlib import Path
import copy
from typing import Optional

from utilities.wcutil import WoodchipperSerializationFile as WCSerialFile
from navigation.constants import FILE_NAME, ERROR
from navigation.core.nav_bookmark import Bookmark, create_bookmark_from_line, create_line_from_bookmark

class BookmarkList:
    type LabelSource = str | Bookmark
    type BookmarkPlain = tuple[str, Path]
    type BookmarkSource = Bookmark | tuple[str, Path]
    type BookmarkChange = tuple[Bookmark, Bookmark]

    def __init__(self):
        file_path: Path = Path.home() / FILE_NAME
        self._ledger:WCSerialFile = WCSerialFile(file_path, create_bookmark_from_line, create_line_from_bookmark)
        self._bookmarks: list[Bookmark] = self._ledger.read()

    def __len__(self):
        return len(self._bookmarks)

    def get_list(self)-> list[Bookmark]:
        return self._bookmarks

    def find(self, test: LabelSource) -> Optional[Bookmark]:
        for bookmark in self._bookmarks:
            if bookmark == test:
                return bookmark
        return None

    def add(self, target:BookmarkSource) -> Bookmark:
        target_bookmark: Bookmark
        if type(target) == tuple[str, Path]:
            target_bookmark = Bookmark(target[0], target[1])
        else:
            target_bookmark = target
        if not self.find(target_bookmark):
            self._bookmarks.append(target_bookmark)
            return target_bookmark
        raise ValueError(ERROR.ADD_EXISTING_BOOKMARK.format(target_bookmark.get_label()))

    def set(self, target: BookmarkSource) -> BookmarkChange:
        target_bookmark: Bookmark
        if type(target) == tuple[str, Path]:
            target_bookmark = Bookmark(target[0], target[1])
        else:
            target_bookmark = target
        source_bookmark: Optional[Bookmark] = self.find(target_bookmark)
        if source_bookmark:
            old_bookmark:Bookmark = copy.copy(source_bookmark)
            source_bookmark.set_path(target_bookmark.get_path())
            return old_bookmark, source_bookmark
        raise ValueError(ERROR.SET_MISSING_BOOKMARK.format(target_bookmark.get_label()))

    def remove(self, target: LabelSource) -> Bookmark:
        target_bookmark: Optional[Bookmark] = self.find(target)
        if target_bookmark:
            self._bookmarks.remove(target_bookmark)
            return target_bookmark
        raise ValueError(ERROR.REMOVE_MISSING_BOOKMARK.format(target_bookmark.get_label()))

    def save(self) -> None:
        self._bookmarks.sort()
        self._ledger.save(self._bookmarks)




