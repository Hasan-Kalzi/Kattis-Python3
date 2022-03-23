# A Rational Sequence 2
# Solution by Hasan Kalzi 27-08-2021
# Link to problem in Kattis: https://open.kattis.com/problems/rationalsequence2
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    k, pq = stdin.readline().split()
    p, q = map(int, pq.split('/'))
    ans = ''
    while p + q > 2:
        if p > q:
            p -= q
            ans += '1'
        else:
            q -= p
            ans += '0'
    ans += '1'
    stdout.write(k + ' ' + str(int(ans[::-1], 2)) + '\n')
