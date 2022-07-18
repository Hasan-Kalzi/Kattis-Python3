# NOP
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/nop
from sys import stdin, stdout

program = stdin.readline().strip()
c = 1
nop = 0
for char in program[1:]:
    if char.islower():
        c += 1
    else:
        if c % 4 != 0:
            nop += 4 - (c % 4)
        c = 1
stdout.write("nop")
