#!/usr/bin/env python3
inp = input()
tot = 0
for n, i in enumerate(inp):
    if i == inp[n - 1]:
        tot += int(i)
print(tot)
