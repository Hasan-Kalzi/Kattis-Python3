# Skocimis
# Solution by Hasan Kalzi 24-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/skocimis
from sys import stdin, stdout, intern

# Three integers A, B and C (0<A<B<C<100), the initial positions of the kangaroos.
a, b, c = [int(_) for _ in intern(stdin.readline()).split()]
if b - a == 1 and c - b == 1:
    stdout.write('0')
elif b - a >= c - b:
    stdout.write(str(b - a - 1))
else:
    stdout.write(str(c - b - 1))

