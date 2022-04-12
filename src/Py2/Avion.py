# Avion
# Solution by Hasan Kalzi 22-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/avion
from sys import stdin, stdout

nothing = 1
for i in range(1, 6):
    if "FBI" in stdin.readline():
        stdout.write(str(i) + ' ')
        nothing = 0
if nothing == 1:
    print("HE GOT AWAY!")
