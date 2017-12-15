#!/usr/bin/env python3
import sys

checksum = 0
for i in sys.stdin:
    line = [int(j.strip()) for j in i.split()]
    checksum += max(line) - min(line)
print(checksum)
