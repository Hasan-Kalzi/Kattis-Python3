# Counting Clauses
# Solution by Hasan Kalzi 14-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/countingclauses
from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
if n > 7:
    stdout.write("satisfactory")
else:
    stdout.write("unsatisfactory")
