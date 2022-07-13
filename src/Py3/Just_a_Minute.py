# Just a Minute
# Solution by Hasan Kalzi 10-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/justaminute
from sys import stdin, stdout

m, n = 0, 0
for _ in range(int(stdin.readline())):
    m_, n_ = map(float, stdin.readline().split())
    m += m_
    n += n_
average = n / (m * 60)
if average <= 1:
    stdout.write("measurement error")
else:
    stdout.write(str(average))
