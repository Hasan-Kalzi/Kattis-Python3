# Cold-puter Science
# Solution by Hasan Kalzi 23-06-2022
# # Link to problem in Kattis: https://open.kattis.com/problems/cold
from sys import stdin, stdout

stdin.readline()
stdout.write(str(len([int(_) for _ in stdin.readline().split() if '-' in _])))