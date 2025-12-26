#!/usr/bin/env python3
"""
Webpage Content Post-Processing Algorithm

This module provides post-processing functions for downloaded webpage content,
including MathML to LaTeX conversion and other Markdown formatting enhancements.
"""

import os
import re
import sys
from typing import Optional, List

class ProcessError(Exception):
    """Exception raised for post-processing errors."""
    pass

def mathml2latex(content: str) -> str:
    """
    Convert MathML entries to LaTeX format in the content.
    
    This function searches for MathML tags and converts them to equivalent
    LaTeX format, performing in-place replacement.
    
    Args:
        content: The content containing MathML entries
        
    Returns:
        Content with MathML converted to LaTeX
    """
    # Pattern to match MathML tags
    # This is a simplified pattern - in a real implementation, you'd want
    # more sophisticated parsing
    mathml_pattern = r'<math[^>]*>(.*?)</math>'
    
    def replace_mathml(match):
        """Replace a MathML match with LaTeX equivalent."""
        mathml_content = match.group(1)
        
        # Convert common MathML patterns to LaTeX
        # This is a basic implementation - real conversion would be more complex
        
        # Handle <mi> (identifier) tags
        mathml_content = re.sub(r'<mi[^>]*>(.*?)</mi>', r'\1', mathml_content)
        
        # Handle <mo> (operator) tags
        mathml_content = re.sub(r'<mo[^>]*>(.*?)</mo>', r'\1', mathml_content)
        
        # Handle <mn> (number) tags
        mathml_content = re.sub(r'<mn[^>]*>(.*?)</mn>', r'\1', mathml_content)
        
        # Handle fractions <mfrac>
        frac_pattern = r'<mfrac[^>]*>\s*<mrow[^>]*>(.*?)</mrow>\s*<mrow[^>]*>(.*?)</mrow>\s*</mfrac>'
        mathml_content = re.sub(frac_pattern, r'\\frac{\1}{\2}', mathml_content)
        
        # Handle superscripts <msup>
        sup_pattern = r'<msup[^>]*>\s*<mrow[^>]*>(.*?)</mrow>\s*<mrow[^>]*>(.*?)</mrow>\s*</msup>'
        mathml_content = re.sub(sup_pattern, r'\1^{\2}', mathml_content)
        
        # Handle subscripts <msub>
        sub_pattern = r'<msub[^>]*>\s*<mrow[^>]*>(.*?)</mrow>\s*<mrow[^>]*>(.*?)</mrow>\s*</msub>'
        mathml_content = re.sub(sub_pattern, r'\1_{\2}', mathml_content)
        
        # Wrap in LaTeX math mode
        return f'${mathml_content}$'
    
    # Replace all MathML occurrences
    processed_content = re.sub(mathml_pattern, replace_mathml, content, flags=re.DOTALL)
    
    return processed_content

def headingconform(content: str) -> str:
    """
    Conform headings to consistent Markdown format.
    
    This function will be implemented in a future phase to showcase
    the extensibility of the algo4process.py script.
    
    Args:
        content: The content with potentially inconsistent headings
        
    Returns:
        Content with conforming heading formats
    """
    # Placeholder for future implementation
    # This will normalize heading formats, ensure consistent levels, etc.
    return content

def process_markdown_file(input_file: str, output_file: str) -> bool:
    """
    Process a Markdown file and append the result to an output file.
    
    Args:
        input_file: Path to the input Markdown file (download.md)
        output_file: Path to the output file to append to
        
    Returns:
        True if successful, False otherwise
        
    Raises:
        ProcessError: If processing fails
    """
    try:
        # Read the input file
        if not os.path.exists(input_file):
            raise ProcessError(f"Input file not found: {input_file}")
        
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            raise ProcessError(f"Input file is empty: {input_file}")
        
        # Apply post-processing functions
        processed_content = content
        
        # Apply MathML to LaTeX conversion
        processed_content = mathml2latex(processed_content)
        
        # Apply heading conformance (when implemented)
        # processed_content = headingconform(processed_content)
        
        # Add separator between multiple contents
        separator = "\n\n---\n\n"
        
        # Append to output file
        with open(output_file, 'a', encoding='utf-8') as f:
            # If output file is not empty, add separator
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                f.write(separator)
            f.write(processed_content)
        
        return True
        
    except IOError as e:
        raise ProcessError(f"File operation error: {str(e)}")
    except Exception as e:
        raise ProcessError(f"Unexpected error during processing: {str(e)}")

def main():
    """Command line interface for the post-processing algorithm."""
    if len(sys.argv) != 2:
        print("Usage: python algo4process.py <output_file>", file=sys.stderr)
        sys.exit(1)
    
    output_file = sys.argv[1]
    
    try:
        # Process the download.md file and append to output file
        success = process_markdown_file('download.md', output_file)
        
        if success:
            print("SUCCESS")  # Signal to web2md.py
            sys.exit(0)
        else:
            print("ERROR: Processing failed", file=sys.stderr)
            sys.exit(1)
            
    except ProcessError as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()