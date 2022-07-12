# Help a PhD candidate out!
# Solution by Hasan Kalzi 18-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/helpaphd
import sys

# The first line of input will be a single integer N (1≤N≤1000) denoting the number of testcases.
for _ in range(int(sys.stdin.readline())):
    values = sys.stdin.readline()
    if values[0] == 'P':
        sys.stdout.write('skipped\n')
    else:
        a, b = [int(_) for _ in values.split('+')]
        sys.stdout.write(str(a+b)+'\n')
