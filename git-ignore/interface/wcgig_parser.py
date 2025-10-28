# wcgig_parser.py
# Created: 12/26/24
# Version: 0.0.1.001
# Last Changes: 10/28/2025

import pathlib

from utilities.wcparser import CLParser as WCParser

def build_parser():
    parser = WCParser("gignore",
                      version="0.0.1.001",
                      description="Take control of your .gitignore files.",
                      footer="Created by Will Plachno. Copyright 2025.")
    parser.add_argument("mode", choices=["show", "add", "setup", "remove", "clear"], default="show",
                        description=" 'show' (default): display all nodes in the local .gitignore file.\n    'add': appends the target to the local .gitignore file.\n    'setup': appends batches of nodes to the .gitignore file.\n    'remove': deletes a node from the .gitignore file.\n    'clear': clears all nodes from the .gitignore file.")
    parser.add_argument("target", nargs="+",
                        description="The target for the script. Should be a valid .gignore node.")
    return parser

def path_shaper(text):
    return pathlib.Path(text).resolve()
