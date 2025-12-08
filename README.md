# The Woodchipper Python Library

This github repo contains several Python scripts written by Will Plachno. All you need is Python 3, and, if testing, PyTest.

## Included Modules

### AEP: /article-examination

A script for analyzing a markdown library. Analyzes the markdown links inside each .md file to find which linked files don't exist and which files are unlinked.

### FrontMat: /frontmatter-edits

ObsidianMD allows for YAML to be put in the beginning of the markdown file for keeping attributes. This script allows for bulk-operation YAML edits. 

### Gig: /git-ignore

A script for analyzing a .gitignore file, including adding, removing, clearing, and initializing. Also sets up the ignore list with the files created by Woodchipper Notes

### WCN: /notes

A script for viewing and saving localized command-line notes. 

### WCTMP: /templates

A script for executing file templating using a custom domain-specific language. Incomplete.

### WCTS: /toolset

Originally used as infrastructure to keep a set of utility files updated between repositories. Now that I have put everything into one monorepo, this script is no longer supported.

### WCUtil: /utilities

The Woodchipper platform. Includes WCCore and other utility code like a wrapper around `diff`, a custom `ArgParse` implementation, and a dictionary class with a default entry for if the key is not found.



For more information on any of the modules, run `[module] --help`.