# Cetvrta
# Solution by Hasan Kalzi 08-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/cetvrta
from sys import stdin, stdout

values = []
for i in range(3):
    values.append(stdin.readline().strip().split())
if values[0][0] == values[1][0]:
    x = values[2][0]
elif values[0][0] == values[2][0]:
    x = values[1][0]
else:
    x = values[0][0]
if values[0][1] == values[1][1]:
    y = values[2][1]
elif values[0][1] == values[2][1]:
    y = values[1][1]
else:
    y = values[0][1]
stdout.write(x + ' ' + y)
