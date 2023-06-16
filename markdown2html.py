#!/usr/bin/python3
# take argument 2 strings argument is the name of the Markdown file and argument is the output file name
"""take argument 2 strings"""
import markdown
import sys


# take argument 2 strings
"""take argument 2 strings"""
if len(sys.argv) != 3:
    """take argument 2 strings"""
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

first = sys.argv[1]
sec = sys.argv[2]

try:
    # take argument 2 strings
    """take argument 2 stringss"""
    with open(first, 'r') as f:
        tempMd = f.read()
except FileNotFoundError:
    # take argument 2 strings
    """take argument 2 strings"""
    print("Missing {} ".format(first))
    sys.exit(1)

textmark = markdown.markdown(tempMd)

with open(sec, 'w') as f:
    # take argument 2 strings
    """take argument 2 strings"""
    f.write(textmark)
