#!/usr/bin/python3

import sys
import os
import markdown

def main():
    # check if the number of arguments is less than 2
    if len(sys.argv) != 3.
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

    # assign arguments to variables
    markdown_file = sys.argv(1)
    html_file = sys.argv(2)

    # check if the Markdown file doesn’t exist
    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    # Read markdown file
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown-content = f.read()

    # convert Markdown to HTML
    html_content = markdown.markdown(markdown-content)

    # Write a html content to the output
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    sys.exit(0)

if __name__ == "__main__":
    main()