# Extra commands for interacting with Terminal.app

This is a tool that adds some extra commands for interacting with the
MacOS Terminal.app. It can also be used as a Python library.

## Requirements

* MacOS, tested on:
  - MacOS 26 "Tahoe"
  - MacOS 15 "Sequoia"
  - MacOS 14 "Sonoma"
  - MacOS 13 "Ventura"
* Python 3.9 or higher
  - No additional dependencies

## Installing

Recommended way to install is through pipx:

    pipx install git+https://github.com/henrik-codes/macos-terminal-cmds.git

Or by cloning this repo and:

    pipx install .

## Command-line usage

Change theme:

    theme "Red sands"

Change title:

    title "Hello world"

Change window size:

    resize 1024x768

Change window size and position:

    resize 100,100 1024x768

## Library usage

```py
import macos_terminal

macos_terminal.terminal_profile_set('Homebrew')
assert macos_terminal.terminal_profile_get() == 'Homebrew'

macos_terminal.terminal_custom_title_set('Hello world')
assert macos_terminal.terminal_custom_title_get() == 'Hello world'

macos_terminal.terminal_bounds_set(50, 100, 800, 600)
assert macos_terminal.terminal_bounds_get() == macos_terminal.MacOSTerminalBounds(x=50, y=100, width=800, height=600)
```

## Unit tests

Run unit tests with `python3 -m unittest discover`

## Without Python (unsupported)

Python acts just as a wrapper around the Apple Script. You could call the
Apple Script directly. This is though unsupported and maybe change or break in
future versions.

### Change profile/theme of the current tab/window

    $ applescript/terminal-profile-get
    Pro
    $ applescript/terminal-profile-set Grass
    $ applescript/terminal-profile-get
    Grass

### Change custom title of the current tab/window

    $ applescript/terminal-custom-title-get
    Terminal
    $ applescript/terminal-custom-title-set Work
    $ applescript/terminal-custom-title-get
    Work

### Change the bounds of the current tab/window

    $ applescript/terminal-bounds-get
    0, 34, 824, 557
    $ applescript/terminal-bounds-set 100 100 800 600
    $ applescript/terminal-bounds-get
    100, 100, 800, 600
