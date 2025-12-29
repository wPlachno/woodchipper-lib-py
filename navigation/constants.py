# constants.py
# Written by: Will Plachno
# Created: 12/15/25
# Version: 0.0.1.001
# Last Changed: 12/17/25

from utilities.wcconstants import COLOR, clr, OP

class META:
    NAME="nav"
    VERSION="0.0.1.001"
    DESCRIPTION="A bookmark system for the command-line. Note that due to terminal limitations, the script cannot effect the working directory of the terminal directly. Use aliases to work around this."
    FOOTER="Created by Will Plachno. Copyright 2025."

class ARGS:
    class MODE:
        NAME="mode"
        DESCRIPTION="Which mode nav will operate in.\n - show: List all bookmarks. If a bookmark label is included, will output the associated directory path.\n - add: Given a bookmark label and a directory path, will add the bookmark to the list. If no directory path is included, will use the current working directory.\n - set: Given a label and a directory path, will edit the label to match the given path. If no path is included, will use the working directory.\n - remove: Given a label, will remove the bookmark from the list."
    class LABEL:
        NAME="label"
        DESCRIPTION="The label of a target bookmark. Only required for add, set, and remove modes, though including it with show mode will print the directory path."
    class PATH:
        NAME="path"
        DESCRIPTION="The directory path to be associated with the label. Only required for add and set modes."

class MODE:
    SHOW="show"
    ADD="add"
    SET="set"
    REMOVE="remove"

class RESULTS:
    CHANGELIST="changelist"
    class SHOW:
        KEY="show"
        ALL="all"
        ONE="one"
    class STATUS:
        KEY="status"
        FOUND="found"
        MISSING="missing"
        ADDED="added"
        REMOVED="removed"
        UPDATED="updated"
    type ChangelistEntry = tuple[str,str,str]

class CHANGE:
    FRAME = {
        "found": f"{clr("> "+OP[0], COLOR.SIBLING)}: {clr(OP[1], COLOR.SUB)}",
        "missing": f"{clr("? "+OP[0], COLOR.CANCEL)}: {clr(OP[1], COLOR.SUB)}",
        "added": f"{clr("+ "+OP[0], COLOR.ACTIVE)}: {clr(OP[1], COLOR.SUB)}",
        "removed": f"{clr("- "+OP[0], COLOR.ACTIVE)}: {clr(OP[1], COLOR.SUB)}",
        "updated": f"{clr("= "+OP[0], COLOR.ACTIVE)}: {clr(OP[1], COLOR.SUB)}"
    }
class SHOWALL:
    ITEM = f"- {clr(OP[0], COLOR.SIBLING)}: {clr(OP[1], COLOR.SUB)}"
    NONE = clr("No bookmarks registered", COLOR.SUBSIB)

class ERROR:
    ADD_EXISTING_BOOKMARK = f"{clr(OP[0], COLOR.SIBLING)} already exists."
    SET_MISSING_BOOKMARK = f"{clr(OP[0], COLOR.SIBLING)} does not yet exist."
    REMOVE_MISSING_BOOKMARK = f"{clr(OP[0], COLOR.SIBLING)} does not yet exist."
    INVALID_BOOKMARK_DESERIALIZATION = f"{clr(OP[0], COLOR.SIBLING)} cannot be deserialized into a Bookmark."
    INVALID_BOOKMARK_SERIALIZATION = f"{clr(OP[0], COLOR.SIBLING)} cannot be serialized to a string like a Bookmark."

FILE_NAME=".wc_bookmarks.txt"