# Graduation
# Solution by Hasan Kalzi 07-04-2021
# Link to problem in https://open.kattis.com/problems/skolavslutningen/en
from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())
cols = [[] for _ in range(m)]
for _ in range(n):
    row = stdin.readline()
    for i in range(m):
        if row[i] not in cols[i]:
            cols[i].append(row[i])
colours = 1
already = set(cols[0])
for i in range(1, m):
    col_length = len(cols[i])
    for j in range(col_length):
        if cols[i][j] in already:
            already.update(cols[i])
            break
        if j == col_length-1:
            already.update(cols[i])
            colours += 1
stdout.write(str(colours))
