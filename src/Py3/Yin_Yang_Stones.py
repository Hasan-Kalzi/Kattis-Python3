# Yin and Yang Stones
# Solution by Hasan Kalzi 07-04-2021
# Link to problem in https://open.kattis.com/problems/yinyangstones
from sys import stdin, stdout

w, b, stones = 0, 0, stdin.readline().strip()
if stones == "WB" * int(len(stones) / 2) or stones == "BW" * int(len(stones) / 2):
    stdout.write('0')
else:
    for char in stones:
        if char == 'W':
            w += 1
        elif char == 'B':
            b += 1

    if w == b and w > 2:
        stdout.write('1')
    else:
        stdout.write('0')
