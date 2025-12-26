#!/usr/bin/env python3
"""
The Website to Markdown Download Utility (web2md.py) v0.2.2

This utility downloads webpages and converts them to Markdown format.
"""

import os
import sys
import signal
from algo4download import webpage_to_markdown, NetworkError, ContentExtractionError, FileOperationError

VERSION = "v0.2.2"

def clear_terminal():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def splash01_start():
    """Display the initial splash screen."""
    clear_terminal()
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.2        ┃
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
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

def splash02_download():
    """Display the download splash screen."""
    clear_terminal()
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.2        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃             Downloading the webpage from the provided URL...             ┃
┃                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

def splash03_download_error(error_message):
    """Display the download error splash screen."""
    clear_terminal()
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.2        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃      A DOWNLOADING ERROR OCCURRED. SEE THE MESSAGE BELOW FOR DETAILS     ┃
┃                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
    print(f"\n{error_message}\n")
    print("Would you like to try again? [Y]/N (Selecting 'N' will terminate the utility.)")

def splash90_end():
    """Display the exit splash screen."""
    clear_terminal()
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.2        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃                                MIT License                               ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
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
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

def cleanup_files():
    """Delete the content of download.html and download.md files."""
    try:
        with open('download.html', 'w') as f:
            f.write('')
        with open('download.md', 'w') as f:
            f.write('')
    except FileNotFoundError:
        pass  # Files don't exist, which is fine

def signal_handler(sig, frame):
    """Handle CTRL+C signal."""
    cleanup_files()
    splash90_end()
    sys.exit(0)

def download_url(url):
    """Download a URL and convert it to markdown."""
    try:
        # Display download splash
        splash02_download()
        
        # Call the webpage_to_markdown function from algo4download.py
        html_file, md_file = webpage_to_markdown(
            url=url,
            html_file='download.html',
            markdown_file='download.md',
            overwrite=True,
            verbose=False  # We handle our own UI feedback
        )
        
        return True, "Download successful!"
        
    except (NetworkError, ContentExtractionError, FileOperationError) as e:
        return False, str(e)
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def handle_error_response(error_message):
    """Handle error response and user retry choice."""
    splash03_download_error(error_message)
    
    while True:
        try:
            user_input = input("\n> ").strip().upper()
            
            # Check if user wants to exit
            if user_input == 'N' or user_input == 'X':
                cleanup_files()
                splash90_end()
                return False  # Exit the program
            
            # Any other input is considered "Yes" (try again)
            return True  # Continue with the program
            
        except KeyboardInterrupt:
            cleanup_files()
            splash90_end()
            return False  # Exit the program

def handle_success_response():
    """Handle successful download response."""
    print("\n✓ Download completed successfully!")
    print("The webpage has been converted to Markdown and saved to 'download.md'")
    
    while True:
        try:
            user_input = input("\nWould you like to download another URL? [Y]/N: ").strip().upper()
            
            # Check if user wants to exit
            if user_input == 'N' or user_input == 'X':
                cleanup_files()
                splash90_end()
                return False  # Exit the program
            
            # Any other input is considered "Yes" (download another)
            return True  # Continue with the program
            
        except KeyboardInterrupt:
            cleanup_files()
            splash90_end()
            return False  # Exit the program

def main():
    """Main function to run the web2md utility."""
    # Set up signal handler for CTRL+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Display initial splash screen
    splash01_start()
    
    # Main loop for user input
    while True:
        try:
            user_input = input("\nEnter URL (or 'X then ENTER' to terminate this utility): ").strip()
            
            # Check if user wants to exit
            if user_input.upper() == 'X':
                cleanup_files()
                splash90_end()
                break
            
            # Process URL if provided
            if user_input:
                success, message = download_url(user_input)
                
                if success:
                    # Handle successful download
                    if not handle_success_response():
                        break
                    # Restart from the beginning
                    splash01_start()
                else:
                    # Handle error
                    if not handle_error_response(message):
                        break
                    # Restart from the beginning
                    splash01_start()
                
        except KeyboardInterrupt:
            cleanup_files()
            splash90_end()
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()