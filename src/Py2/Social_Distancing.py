# Social Distancing
# Solution by Hasan Kalzi 12-04-2022
# Link to the problem in https://open.kattis.com/problems/aaah
from sys import stdin, stdout

s, n = map(int, stdin.readline().split())
seated = [int(_) - 1 for _ in stdin.readline().split()]
can_be_used = 0
for i in range(s):
    before = (i + 1) % s
    after = (i - 1) % s
    if i not in seated:
        if before not in seated and after not in seated:
            seated.append(i)
            can_be_used += 1
stdout.write(str(can_be_used))
