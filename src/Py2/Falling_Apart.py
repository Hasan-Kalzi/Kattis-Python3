# Falling Apart
# Solution by Hasan Kalzi: 10-01-2022
# Link to the problem: https://open.kattis.com/problems/flyingsafely
from sys import stdin, stdout

stdin.readline()
parts = sorted([int(_) for _ in stdin.readline().split()],reverse=True)

alice = 0
bob = 0
turn = 0
for part in parts:
    if turn == 0:
        alice += part
        turn = 1
    else:
        bob += part
        turn = 0
stdout.write(str(alice) + ' ' + str(bob))
