# Turn It Up!
# Solution by Hasan Kalzi 06-12-2021
# Link to problem in Kattis: https://open.kattis.com/problems/skruop
from sys import stdin, stdout

volume = 7
for _ in range(int(stdin.readline())):
    if stdin.readline().strip() == "Skru op!":
        if volume < 10:
            volume += 1
    else:
        if volume > 0:
            volume -= 1
stdout.write(str(volume))
