# nav_bookmark.py
# Written by: Will Plachno
# Created: 12/15/2025
# Version: 0.0.1.002
# Last Changed: 12/29/2025

from pathlib import Path
from navigation.constants import ERROR

class Bookmark:
    type PathSource = str | Path
    def __init__(self, label:str="", path:PathSource=""):
        self._label:str = label.lower()
        self._path:Path = Path(path).resolve()

    def __eq__(self, other: any) -> bool:
        if type(other) == str:
            return other.lower() == self._label
        elif type(other) == Bookmark:
            return other.get_label() == self._label
        return False

    def __lt__(self, other):
        if type(other) == Bookmark:
            return self.get_path() < other.get_path()
        else:
            raise NotImplementedError("Cannot compare a Bookmark to a "+str(type(other)))

    def get_label(self) -> str:
        return self._label

    def set_path(self, path:PathSource) -> bool:
        self._path = Path(path).resolve()
        return self._path.is_dir()

    def get_path(self) -> str:
        return str(self._path)

    def __str__(self) -> str:
        return f"{self._label}:{str(self._path)}"

    def __repr__(self) -> str:
        return f"{self._label}: {str(self._path)}"

def create_bookmark_from_line(line:str) -> Bookmark:
    line_pieces = line.split(":")
    if len(line_pieces) < 2:
        raise ValueError(ERROR.INVALID_BOOKMARK_DESERIALIZATION.format(line))
    label = line_pieces[0]
    path = ":".join(line_pieces[1:]).strip()
    return Bookmark(label=label, path=path)

def create_line_from_bookmark(target:any) -> str:
    if type(target) == Bookmark:
        return str(target)
    else:
        raise ValueError(ERROR.INVALID_BOOKMARK_SERIALIZATION.format(str(target)))