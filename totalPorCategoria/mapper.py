#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split("\t")
    print(words[3] + '-' + words[4])