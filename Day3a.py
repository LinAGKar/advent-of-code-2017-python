#!/usr/bin/env python3
import math
import sys

register = int(input())
if register < 1:
    sys.exit(1)
elif register == 1:
    print(0)
else:
    ring = int((math.sqrt(register - 1) - 1) // 2 + 1)
    first = (1 + 2 * (ring - 1)) ** 2 + 1
    ring_size = ring * 8
    pos_on_side = (register - first) % (ring_size // 4)
    print(abs(pos_on_side - ring + 1) + ring)
