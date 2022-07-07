# Eye of Sauron
# Solution by Hasan Kalzi: 14-02-2022
# Link to the problem: https://open.kattis.com/problems/eyeofsauron
from sys import stdin, stdout

input_string = stdin.readline().strip()

sticks = [0, 0]
i = 0
for char in input_string:
    if char == '(' or char == ')':
        i = 1
    else:
        sticks[i] += 1
if sticks[0] == sticks[1]:
    stdout.write("correct")
else:
    stdout.write("fix")