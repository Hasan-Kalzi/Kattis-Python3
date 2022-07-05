# Dice Cup
# Solution by Hasan Kalzi 08-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/dicecup
from sys import stdin, stdout
values = [int(_) for _ in stdin.readline().split()]
if values[0] > values[1]:
    x = values[1]
    y = values[0]
else:
    x = values[0]
    y = values[1]
for i in range(x + 1, y + 2):
    stdout.write(str(i)+'\n')
