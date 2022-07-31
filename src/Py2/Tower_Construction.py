# Tower Construction
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/tornbygge/en
from sys import stdin, stdout

stdin.readline()
blocks = [int(_) for _ in stdin.readline().split()]
prev = blocks[0]
towers = 1
for block in blocks[1:]:
    if block > prev:
        towers += 1
    prev = block
stdout.write(str(towers))
