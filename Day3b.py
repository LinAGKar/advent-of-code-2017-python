#!/usr/bin/env python3
number = int(input())
move_distance = 1
pos = 0j
values = {0j: 1}
dir = 1
while True:
    for _ in range(2):
        for i in range(move_distance):
            if values[pos] >= number:
                print(values[pos])
                quit()
            pos += dir
            values[pos] = sum(sum(values.get(pos + i + j * 1j, 0) for j in range(-1, 2) if i + j * 1j != 0) for i in range(-1, 2))
        dir *= 1j
    move_distance += 1
