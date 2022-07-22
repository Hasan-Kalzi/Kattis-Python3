# Quadrant Selection
# Solution by Hasan Kalzi: 05-01-2022
# Link to the problem: https://open.kattis.com/problems/quadrant
from sys import stdin, stdout

x, y = int(stdin.readline()), int(stdin.readline())
if x == 0 or y == 0 or x > 1000 or y > 1000 or x < -1000 or y < -1000:
    stdout.write('0')
elif x > 0 and y > 0:
    stdout.write('1')
elif x < 0 < y:
    stdout.write('2')
elif x < 0 and y < 0:
    stdout.write('3')
else:
    stdout.write('4')
