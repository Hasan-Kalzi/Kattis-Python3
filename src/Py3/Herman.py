# Herman
# Solution by Hasan Kalzi 06-11-2021
# Link to problem in Kattis: https://open.kattis.com/problems/herman
from sys import stdin, stdout

r = int(stdin.readline())
stdout.write(str(3.1415926535897932384626433832795 * r ** 2) + '\n')
stdout.write(str(2 * r ** 2))
