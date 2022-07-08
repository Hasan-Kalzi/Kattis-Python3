# coding=utf-8
# Fifty Shades of Pink
# Solution by Hasan Kalzi 22-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/fiftyshades
from sys import stdin, stdout

# The number of training sessions Thore can attend. Select buttons with either “pink” or “rose” somewhere in the name
number_pink_buttons = 0
# after range is the inserted number of packages: int(input())
for _ in range(int(stdin.readline())):
    # the name of the button in row i
    button = stdin.readline().lower()
    if "pink" in button or "rose" in button:
        number_pink_buttons += 1

# If he can’t attend any session because there are no pink buttons, output his standard excuse
# “I must watch Star Wars with my daughter”.
if number_pink_buttons == 0:
    stdout.write("I must watch Star Wars with my daughter")
else:
    stdout.write(str(number_pink_buttons))
