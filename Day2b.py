#!/usr/bin/env python3
import sys

checksum = 0
for i in sys.stdin:
    line = [int(j.strip()) for j in i.split()]
    for j in line:
        for k in line:
            if j is not k and j % k == 0:
                checksum += j // k
print(checksum)
