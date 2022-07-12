# Honour Thy (Apaxian) Parent
# Solution by Hasan Kalzi 18-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/apaxianparent
from sys import stdin, stdout

# The input contains two strings separated by a single space: Y and P, as defined above.
p, y = stdin.readline().split()
if p[len(p) - 2] == 'e' and p[len(p) - 1] == 'x':
    stdout.write(p + y)
elif p[len(p) - 1] == 'e':
    stdout.write(p + "x" + y)
elif p[len(p) - 1] == 'a' or p[len(p) - 1] == 'i' or p[len(p) - 1] == 'u' or p[len(p) - 1] == 'o':
    stdout.write(p[:len(p) - 1] + "ex" + y)
else:
    stdout.write(p + "ex" + y)
