# Powers of 2
# Solution by Hasan Kalzi 21-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/powersof2easy
from sys import stdin, stdout

n, e = map(int, stdin.readline().split())
e = pow(2, e)
k = 0
i = e

if n >= e:
    while i < n + 1:
        if str(e) in str(i):
            k += 1
            i += 1
        else:
            if i % 10 > e % 10:
                i += 10 - (e % 10) - 1
            else:
                i += 1

stdout.write(str(k))
