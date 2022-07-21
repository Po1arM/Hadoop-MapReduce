#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split("\t")
    if words[5] == 'Visa':
        print(words[3] + '-' + words[4])