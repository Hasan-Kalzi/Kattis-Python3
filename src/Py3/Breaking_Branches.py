# Breaking Branches
# Solution by Hasan Kalzi 18-12-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/breakingbranches
import sys

if int(sys.stdin.readline()) % 2 == 0:
    sys.stdout.write("Alice\n1")
else:
    sys.stdout.write("Bob")
