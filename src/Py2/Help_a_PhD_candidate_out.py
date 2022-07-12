# coding=utf-8
# Help a PhD candidate out!
# Solution by Hasan Kalzi 18-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/helpaphd
from sys import stdin, stdout

# The first line of input will be a single integer N (1≤N≤1000) denoting the number of testcases.
for _ in range(int(stdin.readline())):
    values = stdin.readline()
    if values[0] == 'P':
        stdout.write('skipped\n')
    else:
        a, b = map(int, values.split('+'))
        stdout.write(str(a+b)+'\n')
