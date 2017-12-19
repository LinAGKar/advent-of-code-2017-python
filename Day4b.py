#!/usr/bin/env python3
import sys

counter = 0
for i in sys.stdin:
    words = set()
    for j in i.strip().split():
        word = ''.join(sorted(j))
        if word in words:
            break
        words.add(word)
    else:
        counter += 1
print(counter)
