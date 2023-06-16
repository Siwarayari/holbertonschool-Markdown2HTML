#!/usr/bin/python3
#  takes an argument 2 strings
""" takes an argument 2 strings"""
import markdown
import sys


#   takes an argument 2 strings
""" takes an argument 2 strings"""
if len(sys.argv) != 3:
    """ takes an argument 2 strings"""
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

first = sys.argv[1]
sec = sys.argv[2]

try:
    #  takes an argument 2 strings
    """ takes an argument 2 strings"""
    with open(first, 'r') as f:
        tempMd = f.read()
except FileNotFoundError:
    # takes an argument 2 strings
    """ takes an argument 2 strings"""
    print("Missing {} ".format(first))
    sys.exit(1)

textmark = markdown.markdown(tempMd)

with open(sec, 'w') as f:
    # takes an argument 2 strings
    """ takes an argument 2 strings"""
    f.write(textmark)
