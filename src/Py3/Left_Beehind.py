# Left Beehind
# Solution by Hasan Kalzi 21-03-2021
# Link to problem in https://open.kattis.com/problems/leftbeehind
import sys

while True:
    sweet, sour = map(int, sys.stdin.readline().split())
    if sweet == 0 and sour == 0:
        break
    if sweet + sour == 13:
        sys.stdout.write("Never speak again.\n")
    elif sweet > sour:
        sys.stdout.write("To the convention.\n")
    elif sweet == sour:
        sys.stdout.write("Undecided.\n")
    else:
        sys.stdout.write("Left beehind.\n")
