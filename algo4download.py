#!/usr/bin/env python3
"""
Webpage to Markdown Converter Algorithm

This module provides a reusable algorithm for downloading webpages,
extracting the main content, and converting it to Markdown format.
"""

import os
import re
import sys
import argparse
from typing import Optional, Tuple, Dict
try:
    import requests
    from bs4 import BeautifulSoup
    import html2text
except ImportError as e:
    print(f"Error: Required package not found. Please install: {e}")
    print("Run: pip install requests beautifulsoup4 html2text")
    sys.exit(1)

# HTTP status code descriptions
HTTP_STATUS_CODES = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK - Request successful",
    201: "Created - Resource created successfully",
    202: "Accepted - Request accepted for processing",
    203: "Non-Authoritative Information",
    204: "No Content - Request successful but no content to return",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices - Multiple options available",
    301: "Moved Permanently - Resource permanently moved",
    302: "Found - Resource temporarily moved",
    303: "See Other - See other URL for resource",
    304: "Not Modified - Resource has not been modified",
    305: "Use Proxy - Use proxy to access resource",
    306: "(Unused)",
    307: "Temporary Redirect - Resource temporarily redirected",
    308: "Permanent Redirect - Resource permanently redirected",
    400: "Bad Request - Invalid request syntax",
    401: "Unauthorized - Authentication required",
    402: "Payment Required - Payment required for access",
    403: "Forbidden - Server refuses to fulfill request",
    404: "Not Found - Resource not found",
    405: "Method Not Allowed - Request method not allowed",
    406: "Not Acceptable - Request format not acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout - Server timed out waiting for request",
    409: "Conflict - Request conflict with current state",
    410: "Gone - Resource no longer available",
    411: "Length Required - Content-Length header required",
    412: "Precondition Failed",
    413: "Payload Too Large - Request entity too large",
    414: "URI Too Long - URI too long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests - Rate limit exceeded",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error - Server encountered unexpected error",
    501: "Not Implemented - Server does not support request method",
    502: "Bad Gateway - Server received invalid response",
    503: "Service Unavailable - Server temporarily unavailable",
    504: "Gateway Timeout - Server gateway timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required"
}

def get_status_description(status_code: int) -> str:
    """
    Get a descriptive message for an HTTP status code.
    
    Args:
        status_code: HTTP status code
        
    Returns:
        Description of the status code
    """
    return HTTP_STATUS_CODES.get(status_code, f"Unknown Status Code: {status_code}")

def download_webpage(url: str, timeout: int = 30, user_agent: str = None) -> Tuple[str, Dict]:
    """
    Download HTML content from a URL.
    
    Args:
        url: URL to download
        timeout: Request timeout in seconds
        user_agent: Custom user agent string
        
    Returns:
        Tuple of (html_content, response_info)
        
    Raises:
        NetworkError: If download fails
    """
    if user_agent is None:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    
    headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        
        response_info = {
            "status_code": response.status_code,
            "status_description": get_status_description(response.status_code),
            "headers": dict(response.headers),
            "url": response.url,
            "encoding": response.encoding
        }
        
        return response.text, response_info
        
    except requests.exceptions.RequestException as e:
        error_msg = f"Failed to download webpage: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            status_code = e.response.status_code
            error_msg = f"HTTP {status_code} ({get_status_description(status_code)}): {str(e)}"
        raise NetworkError(error_msg) from e

def extract_main_content(html_content: str, content_selectors: list = None) -> str:
    """
    Extract the main content from HTML.
    
    Args:
        html_content: HTML content to parse
        content_selectors: List of CSS selectors to try for finding main content
        
    Returns:
        Extracted main content as HTML string
        
    Raises:
        ContentExtractionError: If main content cannot be found
    """
    if content_selectors is None:
        # Default selectors for common content areas
        content_selectors = [
            "article.nextra-content",  # Nextra documentation (used in our example)
            "article.content",
            "main[role='main']",
            ".content",
            "#content",
            "article",
            "main",
            ".main-content",
            "#main-content"
        ]
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Try each selector until we find content
    for selector in content_selectors:
        elements = soup.select(selector)
        if elements:
            return str(elements[0])
    
    # If no selector works, try to find the largest text block
    # Remove script, style, nav, header, footer elements
    for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
        tag.decompose()
    
    # Find the element with the most text content
    max_text = 0
    best_element = None
    
    for element in soup.find_all(['div', 'section', 'article']):
        text_length = len(element.get_text(strip=True))
        if text_length > max_text:
            max_text = text_length
            best_element = element
    
    if best_element:
        return str(best_element)
    
    raise ContentExtractionError("Could not extract main content from webpage")

def html_to_markdown(html_content: str, options: dict = None) -> str:
    """
    Convert HTML content to Markdown.
    
    Args:
        html_content: HTML content to convert
        options: Conversion options
        
    Returns:
        Markdown content
    """
    if options is None:
        options = {
            "ignore_links": False,
            "ignore_images": False,
            "ignore_emphasis": False,
            "body_width": 0,  # No line wrapping
            "protect_links": True,
            "wrap": False,
            "skip_internal_links": True,
            "inline_links": True,
            "pad_tables": True,
        }
    
    h = html2text.HTML2Text()
    
    # Configure html2text based on options
    h.ignore_links = options.get("ignore_links", False)
    h.ignore_images = options.get("ignore_images", False)
    h.ignore_emphasis = options.get("ignore_emphasis", False)
    h.body_width = options.get("body_width", 0)
    h.protect_links = options.get("protect_links", True)
    h.wrap = options.get("wrap", False)
    h.skip_internal_links = options.get("skip_internal_links", True)
    h.inline_links = options.get("inline_links", True)
    h.pad_tables = options.get("pad_tables", True)
    
    markdown_content = h.handle(html_content)
    
    # Clean up the markdown
    # Remove excessive newlines
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    
    # Fix common formatting issues
    markdown_content = markdown_content.strip()
    
    return markdown_content

def save_file(content: str, file_path: str, overwrite: bool = False) -> None:
    """
    Save content to a file.
    
    Args:
        content: Content to save
        file_path: Path to save the file
        overwrite: Whether to overwrite existing files
        
    Raises:
        FileOperationError: If file operation fails
    """
    if os.path.exists(file_path) and not overwrite:
        raise FileOperationError(f"File already exists: {file_path}")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path) or '.', exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except IOError as e:
        raise FileOperationError(f"Failed to save file: {str(e)}") from e

class NetworkError(Exception):
    """Exception raised for network-related errors."""
    pass

class ContentExtractionError(Exception):
    """Exception raised when content extraction fails."""
    pass

class FileOperationError(Exception):
    """Exception raised for file operation errors."""
    pass

def webpage_to_markdown(url: str, 
                       html_file: str = None, 
                       markdown_file: str = None,
                       content_selectors: list = None,
                       conversion_options: dict = None,
                       overwrite: bool = False,
                       verbose: bool = True) -> Tuple[str, str]:
    """
    Convert a webpage to Markdown.
    
    Args:
        url: URL of the webpage to convert
        html_file: Path to save the HTML file (optional)
        markdown_file: Path to save the Markdown file (optional)
        content_selectors: List of CSS selectors to try for finding main content
        conversion_options: Options for HTML to Markdown conversion
        overwrite: Whether to overwrite existing files
        verbose: Whether to print progress information
        
    Returns:
        Tuple of (html_file_path, markdown_file_path)
        
    Raises:
        NetworkError: If download fails
        ContentExtractionError: If content extraction fails
        FileOperationError: If file operations fail
    """
    if verbose:
        print(f"Downloading webpage: {url}")
    
    # Download the webpage
    html_content, response_info = download_webpage(url)
    
    if verbose:
        print(f"Download successful: {response_info['status_description']}")
        print(f"Content length: {len(html_content)} characters")
    
    # Save HTML file if requested
    html_path = html_file
    if html_path:
        save_file(html_content, html_path, overwrite)
        if verbose:
            print(f"HTML saved to: {html_path}")
    
    # Extract main content
    if verbose:
        print("Extracting main content...")
    
    main_content = extract_main_content(html_content, content_selectors)
    
    # Convert to Markdown
    if verbose:
        print("Converting to Markdown...")
    
    markdown_content = html_to_markdown(main_content, conversion_options)
    
    # Save Markdown file if requested
    md_path = markdown_file
    if md_path:
        save_file(markdown_content, md_path, overwrite)
        if verbose:
            print(f"Markdown saved to: {md_path}")
    
    return html_path, md_path

def main():
    """Command line interface for the webpage to Markdown converter."""
    parser = argparse.ArgumentParser(
        description="Convert webpages to Markdown format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://example.com
  %(prog)s https://example.com --html-file example.html --md-file example.md
  %(prog)s https://example.com --content-selectors ".content article" --overwrite
        """
    )
    
    parser.add_argument("url", help="URL of the webpage to convert")
    parser.add_argument("--html-file", help="Path to save the HTML file")
    parser.add_argument("--md-file", help="Path to save the Markdown file")
    parser.add_argument("--content-selectors", nargs="+", 
                       help="CSS selectors to try for finding main content")
    parser.add_argument("--overwrite", action="store_true",
                       help="Overwrite existing files")
    parser.add_argument("--quiet", action="store_true",
                       help="Suppress progress information")
    
    args = parser.parse_args()
    
    try:
        webpage_to_markdown(
            url=args.url,
            html_file=args.html_file,
            markdown_file=args.md_file,
            content_selectors=args.content_selectors,
            overwrite=args.overwrite,
            verbose=not args.quiet
        )
    except (NetworkError, ContentExtractionError, FileOperationError) as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()