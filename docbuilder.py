#!/usr/bin/env python

import os
import sys

FILE = "write-good.py"
EXPORT = "docs/index.md"
string = "Unset"
if os.path.isfile(EXPORT):
    os.remove(EXPORT)
file = open(FILE, "r")
outfile = open(EXPORT, "w+")
for line in file.read().split('\n'):
    string = line
    string = string.strip()
    char = string[:1]
    if char == u'\u0023':
        string = line[1:]
        outfile.write("\n")
        outfile.write(string)
        outfile.write("\n")
    else:
        outfile.write("\n")
        outfile.write("```")
        outfile.write(string)
        outfile.write("```")
        outfile.write("\n")
file.close()
outfile.close()
