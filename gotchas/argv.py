"""
Try running
$ python argv.py --foo --bar --baz
"""
from sys import argv

script, *args = argv
print(args)
