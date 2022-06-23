# Cinema Crowds 2
# Solution by Hasan Kalzi 31-10-2021
# Link to problem in Kattis: https://open.kattis.com/problems/cinema2
from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
groups = [int(_) for _ in stdin.readline().split()]
sub_sum = 0
if len(groups) == 1:
    stdout.write('1')
elif len(groups) == 2:
    if groups[0] > n and groups[1] > n:
        stdout.write('2')
    else:
        stdout.write('1')
else:
    i = 0
    for group in groups:
        sub_sum += group
        if sub_sum > n:
            stdout.write(str(len(groups) - i))
            break
        i += 1
