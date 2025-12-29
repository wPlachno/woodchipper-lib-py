# woodchipper-navigation
A command line python script for keeping directory bookmarks

## Welcome
Thank you for taking the time to look at Will Plachno's woodchipper-navigation project. The description provided here is the ultimate scope of the project - it describes the intended functionality. To see what is actually written and working, follow the log notes at the bottom of this file.

This project administrates a command-line system of bookmarks, allowing for the addition, setting, and removing of different directory paths to the system. In order for the script to be actually useful, the user should set up aliases on their terminal for general usage of the script and to automatically `cd` into the output of the script.

```
nav -- Lists the bookmarks currently registered on the system.
nav [LABEL] -- Outputs the directory path of the bookmark associated with the label.
nav add [LABEL] [Optional: PATH] -- Registers the label and path as a bookmark on the system. If [PATH] is omitted, will use the current working directory.
nav set [LABEL] [Optional: PATH] -- Modifies the bookmark with the corresponding label to match the given path. Will use the working directory path if [PATH] is omitted.
nav remove [LABEL] -- Removes the bookmark associated with the given label.
```

## Aliases
Python scripts cannot affect the working directory of the terminal because they are run in a sub-process. To actually change the working directory, we should set up an alias to change the working directory to the output of the script. For every-day usage of this particular script, it is suggested to set up two aliases:
1. `nav` - for using the script in modes that don't require the command-line working directory to change.
2. `navto` - for using the script to change the working directory of the current terminal.

#### Aliases for Windows Command Prompt:
``` Batch
doskey nav="[Python Execution Label] [Script Path]" $*
doskey navto=for /f "delims=" %%D in ('[Python Execution Label] [Script Path] $*') do cd /D %%D
```
- `doskey nav="[Python Execution Label] [Script Path]" $*` — Replace `[Python Execution Label]` with whichever Python Execution command you need. For my own system, the label is `py`. Replace `[Script Path]` with the full file path to the script. In my own alias script, I already have a variable to the root of the Woodchipper GitHub core directory, `wcRoot`. My full `nav` alias is `doskey nav="py %wcRoot%/navigation/nav.py" $*`.
- `doskey navto=for /f "delims=" %%D in ('[Python Execution Label] [Script Path] $*') do cd /D %%D` — Follow the same replacement patterns as the `nav` alias. This alias loops through the outputs of the script and changes the working directory of the terminal to each. Note that this does take into account all output, so we should make sure the script is only outputting a path.

#### Aliases for Bash Terminal:
``` Bash
alias nav="[Python Execution Label] [Script Path]"
navto() {
  cd "$([Python Execution Label] [Script Path] "$@")"
}
```
- `alias nav="[Python Execution Label] [Script Path]"` — Replace `[Python Execution Label]` with whichever Python Execution command you need. For my own system, the label is `py`. Replace `[Script Path]` with the full file path to the script. In my own alias script, I already have a variable to the root of the Woodchipper GitHub core directory, `wcRoot`. My full `nav` alias is `alias nav="${py} ${wcRoot}/navigation/nav.py"`.
- For the `navto` alias, things are easier if we use a Bash function instead of an alias. Note that this does take into account all output, so we should make sure the script is only outputting a path, without any color or formatting.

## ToDo
- Add autosort of bookmarks by path.
- Add Import/Export features.
- Add tab autocomplete for labels.

## Work Log
- 12/29/2025 - Wrote the README.md
- 12/17/2025 - Finished first draft of implementation.