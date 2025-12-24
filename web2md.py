#!/usr/bin/env python3
"""
The Website to Markdown Download Utility (web2md.py) v0.2.1

This utility downloads webpages and converts them to Markdown format.
"""

import os
import sys
import signal

VERSION = "v0.2.1"

def clear_terminal():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def splash01_start():
    """Display the initial splash screen."""
    clear_terminal()
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.1        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃  This utility will download a webpage from a given URL, convert the      ┃
┃  HTML, and save the result to a Markdown file called 'output.md'.        ┃
┃                                                                          ┃
┃  You can provide sequential URLs and the results will be added to        ┃
┃  the end of the output file.                                             ┃
┃                                                                          ┃
┃  To close this utility, you can type 'X then ENTER' or 'CTRL + C'.       ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃  Copy the URL from the address bar of your browser,                      ┃
┃  paste (CTRL + SHIFT + V) the URL to this terminal,                      ┃
┃  then tap the ENTER key.                                                 ┃
┃                                                                          ┃
┖──────────────────────────────────────────────────────────────────────────┚""")

def splash99_end():
    """Display the exit splash screen."""
    clear_terminal()
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                          ┃
┃       The Website to Markdown Download Utility (web2md.py) v0.2.1        ┃
┃                                                                          ┃
┠──────────────────────────────────────────────────────────────────────────┨
┃                                                                          ┃
┃                                MIT License                               ┃
┃                                                                          ┃
┌──────────────────────────────────────────────────────────────────────────┐
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
┖──────────────────────────────────────────────────────────────────────────┚""")

def cleanup_files():
    """Delete the content of template.html and template.md files."""
    try:
        with open('template.html', 'w') as f:
            f.write('')
        with open('template.md', 'w') as f:
            f.write('')
    except FileNotFoundError:
        pass  # Files don't exist, which is fine

def signal_handler(sig, frame):
    """Handle CTRL+C signal."""
    cleanup_files()
    splash99_end()
    sys.exit(0)

def main():
    """Main function to run the web2md utility."""
    # Set up signal handler for CTRL+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Display initial splash screen
    splash01_start()
    
    # Main loop for user input
    while True:
        try:
            user_input = input("\nEnter URL (or 'X' to exit): ").strip()
            
            # Check if user wants to exit
            if user_input.upper() == 'X':
                cleanup_files()
                splash99_end()
                break
                
            # TODO: In future phases, add URL processing here
            if user_input:
                print(f"URL received: {user_input}")
                print("(URL processing will be implemented in future phases)")
                
        except KeyboardInterrupt:
            cleanup_files()
            splash99_end()
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()