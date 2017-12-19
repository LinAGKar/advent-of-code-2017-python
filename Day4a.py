#!/usr/bin/env python3
import sys

counter = 0
for i in sys.stdin:
    words = set()
    for j in i.strip().split():
        if j in words:
            break
        words.add(j)
    else:
        counter += 1
print(counter)
