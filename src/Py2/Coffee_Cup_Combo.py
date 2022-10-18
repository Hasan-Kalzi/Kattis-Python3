# Coffee Cup Combo
# Solution by Hasan Kalzi 10-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/coffeecupcombo
from sys import stdin, stdout

stdin.readline()
focus, refill = 0, 0
for letter in stdin.readline().strip():
    if letter == '1':
        refill = 2
        focus += 1
    elif refill > 0:
        focus += 1
        refill -= 1
stdout.write(str(focus))
