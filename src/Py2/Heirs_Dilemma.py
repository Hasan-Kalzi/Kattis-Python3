# Heir's Dilemma
# Solution by Hasan Kalzi 25-06-2021
# Link to problem in Kattis: https://open.kattis.com/problems/heirsdilemma
from sys import stdin, stdout

start, end = map(int, stdin.readline().split())
combinations = 0
for i in range(start, end + 1):
    check_diff = "".join(set(str(i)))
    if len(check_diff) == 6 and '0' not in check_diff:
        n1, n2, n3, n4, n5, n6 = int(str(i)[0]), int(str(i)[1]), int(str(i)[2]), int(str(i)[3]), int(str(i)[4]), \
                                 int(str(i)[5])
        if i % n1 == 0 and i % n2 == 0 and i % n3 == 0 and i % n4 == 0 and i % n5 == 0 and i % n6 == 0:
            combinations += 1
stdout.write(str(combinations))
