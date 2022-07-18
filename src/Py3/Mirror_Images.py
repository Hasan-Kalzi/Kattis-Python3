# Mirror Images
# Solution by Hasan Kalzi 10-04-2021
# Link to problem in https://open.kattis.com/problems/mirror
from sys import stdin, stdout

for k in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    original = []
    stdout.write("Test " + str(k+1) + '\n')
    for _ in range(n):
        original.append(stdin.readline().strip())
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            stdout.write(original[i][j])
        stdout.write('\n')