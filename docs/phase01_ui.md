---
name: "Phase 01: UI"
description: "Develop the initial version of web2md.py, focusing on basic functionality and user interaction."
mode: "bmad-dmm-dev"
version: "v0.2.3"
---

# Phase 01: UI

## Objective
Create a Python script named `web2md.py` that provides a basic command-line interface for downloading web pages and converting them to Markdown. This phase focuses on displaying initial and final splash screens, handling user input for termination, and setting up the project version.

## Version
The current version of the `web2md.py` utility is `v0.2.1`. This version number should be reflected in all relevant outputs and internal configurations.

## Task Breakdown

### 1. Create `web2md.py`
Create a new Python file named `web2md.py` in the root directory of the project.

### 2. Implement Splash Screens

#### 2.1. `splash01_start`
Upon script execution, the terminal must be cleared, and the following `splash01_start` message displayed:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.1        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃    This utility will download a webpage from a given URL, convert the    ┃
┃     HTML, and save the result to a Markdown file called 'output.md'.     ┃
┃                                                                          ┃
┃               You can provide sequential URLs and the results            ┃
┃               will be added to the end of the output file.               ┃
┃                                                                          ┃
┃      To close this utility, you can type 'X then ENTER' or 'CTRL + C'.   ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃            Copy the URL from the address bar of your browser,            ┃
┃            paste (CTRL + SHIFT + V) the URL to this terminal,            ┃
┃                         then tap the ENTER key.                          ┃
┃                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

#### 2.2. `splash90_end`
When the user types 'X' (case-insensitive) followed by ENTER, or presses 'CTRL + C', the script must perform the following actions:
1. Delete the content of `download.html` and `download.md` files.
2. Clear the terminal screen.
3. Display the following `splash90_end` message:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.1        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃                                MIT License                               ┃
┃                                                                          ┃
┃──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃           © Copyright 2025 DigitalCoreNZ. All rights reserved.           ┃
┃                                                                          ┃
┃        Permission is hereby granted, free of charge, to any person       ┃
┃      obtaining a copy of this software, and associated documentation     ┃
┃    files (the "Software"), to deal in the Software without restriction,  ┃
┃   including without limitation, the rights to use, copy, modify, merge,  ┃
┃    publish, distribute, sublicense, and/or sell copies of the Software,  ┃
┃      and to permit persons to whom the Software is furnished to do so,   ┃
┃                   subject to the following conditions:                   ┃
┃                                                                          ┃
┃          THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF           ┃
┃       ANY KIND, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,       ┃
┃       THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR        ┃
┃       PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS,       ┃
┃        OR COPYRIGHT HOLDERS, BE LIABLE FOR ANY CLAIM, DAMAGES OR         ┃
┃        OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR        ┃
┃        OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH, THE        ┃
┃          SOFTWARE, OR THE USE, OR OTHER DEALINGS IN THE SOFTWARE.        ┃
┃                                                                          ┃
┃              The above notice shall be included in all copies,           ┃
┃                  or substantial portions, of the Software.               ┃
┃                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```
4. Terminate the Python script.

## End of PHASE 01: UI
This marks the completion of 'PHASE 01: UI' for the `web2md.py` utility development. Subsequent phases will build upon this foundation.