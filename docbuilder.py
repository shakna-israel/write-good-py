import os
import sys

FILE = "write-good.py"
string = "Unset"
file = open(FILE, "r")
for line in file.read().split('\n'):
    line = string
    print "original string: ", string
    string = string[1:]
    print "string: " , string
file.close()
