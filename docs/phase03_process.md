---
name: "Phase 03: Process"
description: "Implement the post-processing functionality for web2md.py, integrating with algo4process.py to process downloaded content and manage output files."
mode: "bmad-dmm-dev"
---

# Phase 03: Process Implementation

## Objective
Enhance the web2md.py utility to post-process downloaded content using the algo4process.py script, manage output files with incremental naming, and provide an improved termination flow with file renaming options.

## Version Update
Update the version number from v0.2.2 to v0.2.3 throughout the project, including all splash screens and internal configurations.

## Current State Review
The web2md.py script currently:
- Accepts a URL from the user
- Passes the URL to the algo4download.py script
- Handles errors from algo4download.py with appropriate user feedback
- Downloads content from the URL and saves it to download.html
- Converts the content to Markdown format and saves it to download.md
- Receives success confirmation from algo4download.py
- Displays success message and asks if user wants to download another URL

## Task Breakdown

### 1. Update Version Number
Update the VERSION constant in web2md.py from "v0.2.2" to "v0.2.3" and ensure this change is reflected in all splash screens.

### 2. Implement Post-Processing Flow

#### 2.1. Replace Success Handling
When web2md.py receives the success signal from algo4download.py:
1. Run the clear_terminal() function
2. Display the splash04_process screen:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.3        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃                      Processing the output file...                       ┃
┃                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

#### 2.2. Output File Management
1. Check if 'output01.md' file exists
2. If it exists, check if 'output02.md' exists
3. Continue incrementing numbers until an available filename is found
4. Create an empty Markdown file with the determined filename
5. Pass this filename to the algo4process.py script
6. Wait for a signal from algo4process.py

### 3. Implement algo4process.py Integration

#### 3.1. Create algo4process.py Script
Create the algo4process.py script with the following functionality:
1. Accept a filename parameter from web2md.py
2. Implement the mathml2latex() function:
   - Read content from download.md
   - Find MathML entries and convert them to LaTeX
   - Perform conversions in-place (replace MathML at the same location)
3. Append the processed content from download.md to the output file
4. Send a SUCCESS signal back to web2md.py

#### 3.2. Design for Extensibility
Structure algo4process.py to easily accommodate:
- Additional Markdown processing functions (e.g., headingconform() to be added later)
- Functions for other file formats (e.g., AsciiDoc)
- Modular design for easy expansion

### 4. Rationale for Post-Processing
The post-processing approach provides several benefits:
- download.md content is deleted when the utility is terminated
- download.md content is deleted before another URL is processed
- download.md remains temporary, disposable, and ethereal
- download.md stays lightweight while the output file grows with additional URLs
- Content can be post-processed before being appended to the output file

### 5. Update Termination Process

#### 5.1. Implement splash05_save
When user input is 'X (case-insensitive) + ENTER' or 'CTRL + C':
1. Display the splash05_save screen:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.3        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃        If you want to rename the output file, add the name below.        ┃
┃         Otherwise, tap the ENTER key to terminate this utility.          ┃
┃                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

#### 5.2. File Renaming Logic
1. If the user provides a new filename:
   - Apply the new name to the output file
   - Add or replace the '.md' extension if needed
2. Continue with the termination process
3. If user just presses ENTER, terminate without renaming

### 6. Integration Requirements

#### 6.1. Communication with algo4process.py
1. Import necessary functions from algo4process.py
2. Pass the output filename to algo4process.py
3. Wait for and handle the SUCCESS signal
4. Handle any potential errors from the processing script

#### 6.2. File Management Updates
1. Update cleanup_files() to handle any additional temporary files
2. Ensure proper file permissions for output files
3. Handle file naming conflicts appropriately

## Implementation Notes
- Maintain all existing functionality from Phase 02
- Ensure the download.md file is properly cleaned up after processing
- Preserve all user input handling and error handling
- Keep the same coding style and structure
- Design algo4process.py with extensibility in mind
- Test with various URLs to ensure proper processing
- Ensure proper error propagation from algo4process.py to web2md.py

## End of Phase 03
This marks the completion of Phase 03 for the web2md.py utility development. The utility now has full post-processing functionality with output file management and an improved termination flow.