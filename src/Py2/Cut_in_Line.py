# Cut in Line
# Solution by Hasan Kalzi 06-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/cutinline
from sys import stdin, stdout

line = []
for _ in range(int(stdin.readline())):
    line.append(stdin.readline().strip())
for _ in range(int(stdin.readline())):
    order = stdin.readline().strip().split()
    if order[0] == 'cut':
        line.insert(line.index(order[2]), order[1])
    else:
        line.remove(order[1])

stdout.write("\n".join(str(_) for _ in line))
