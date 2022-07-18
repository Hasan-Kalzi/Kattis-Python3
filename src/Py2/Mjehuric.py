# Mjehuric
# Solution by Hasan Kalzi 18-03-2021
# Link to problem in https://open.kattis.com/problems/mjehuric
import sys

n1, n2, n3, n4, n5 = map(int, sys.stdin.readline().split())

while n1 != 1 or n2 != 2 or n3 != 3 or n4 != 4 or n5 != 5:
    if n1 > n2:
        n1, n2 = n2, n1
        sys.stdout.write(str(n1) + " " + str(n2) + " " + str(n3) + " " + str(n4) + " " + str(n5) + "\n")
    if n2 > n3:
        n2, n3 = n3, n2
        sys.stdout.write(str(n1) + " " + str(n2) + " " + str(n3) + " " + str(n4) + " " + str(n5) + "\n")
    if n3 > n4:
        n3, n4 = n4, n3
        sys.stdout.write(str(n1) + " " + str(n2) + " " + str(n3) + " " + str(n4) + " " + str(n5) + "\n")
    if n4 > n5:
        n4, n5 = n5, n4
        sys.stdout.write(str(n1) + " " + str(n2) + " " + str(n3) + " " + str(n4) + " " + str(n5) + "\n")