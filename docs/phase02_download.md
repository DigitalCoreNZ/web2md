---
name: "Phase 02: Download"
description: "Implement the download functionality for web2md.py, integrating with algo4download.py to fetch and convert web pages."
mode: "bmad-dmm-dev"
version: "v0.2.3"
---

# Phase 02: Download Implementation

## Objective
Enhance the web2md.py utility to download webpages using the algo4download.py script and handle both successful downloads and error conditions with appropriate user feedback.

## Version Update
Update the version number from v0.2.1 to v0.2.2 throughout the project, including all splash screens and internal configurations.

## Task Breakdown

### 1. Update Version Number
Update the VERSION constant in web2md.py from "v0.2.1" to "v0.2.2" and ensure this change is reflected in all splash screens.

### 2. Implement Download Process

#### 2.1. URL Input Handling
When the user provides a URL and taps ENTER:
1. Clear the terminal using the clear_terminal() function
2. Display the splash02_download screen:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.2        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃             Downloading the webpage from the provided URL...             ┃
┃                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

#### 2.2. Integration with algo4download.py
1. Pass the provided URL to the algo4download.py script
2. Wait for a response from the script
3. Handle both success and error responses appropriately

### 3. Error Handling

#### 3.1. Download Error Display
If web2md.py receives an error message from algo4download.py:
1. Clear the terminal using clear_terminal()
2. Clear the downloaded content using cleanup_files()
3. Display the splash03_download_error screen:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.2        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃      A DOWNLOADING ERROR OCCURRED. SEE THE MESSAGE BELOW FOR DETAILS     ┃
┃                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```
3. Display the error message from algo4download.py below the splash
4. Display the retry prompt:
```
Would you like to try again? [Y]/N (Selecting 'N' will terminate the utility.)
```

#### 3.2. Error Response Handling
1. If user types 'N (case-insensitive) + ENTER', 'X (case-insensitive) + ENTER', or presses 'CTRL + C':
   - Run the splash90_end() function
   - Run the cleanup_files() function
   - Terminate the utility
2. '[Y]es' is the default response - any input other than the exit options:
   - Run clear_terminal()
   - Run splash01_start()
   - Restart the utility from the beginning

### 4. Success Handling

#### 4.1. Successful Download
A successful outcome from algo4download.py includes:
1. URL webpage saved to download.html file
2. Content of download.html successfully converted to Markdown format
3. Conversion saved to download.md file
4. web2md.py receives a SUCCESS response

#### 4.2. Post-Download Flow
After a successful download:
1. Display a success message to the user
2. Ask if they want to download another URL or exit
3. Handle the response appropriately (restart or exit)

### 5. Integration Requirements

#### 5.1. Communication with algo4download.py
1. Import necessary functions from algo4download.py
2. Handle exceptions that may be raised (NetworkError, ContentExtractionError, FileOperationError)
3. Capture and display appropriate error messages
4. Ensure proper file paths are used (download.html and download.md)

#### 5.2. File Management
1. Ensure download.html and download.md files are properly created and managed
2. Update cleanup_files() function to handle these files if needed
3. Verify file permissions and accessibility

## Implementation Notes
- Maintain all existing functionality from Phase 01
- Ensure all user input handling remains consistent
- Preserve the signal handling for CTRL+C
- Keep the same coding style and structure
- Test with various URLs including those that may return errors
- Ensure proper error propagation from algo4download.py to web2md.py

## End of Phase 02
This marks the completion of Phase 02 for the web2md.py utility development. The utility now has full download functionality with proper error handling and user feedback.