# Tri
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/tri
import sys

f, s, t = map(int, sys.stdin.readline().split())  # First int , second int, third int
if f + s == t:
    sys.stdout.write(str(f) + '+' + str(s) + '=' + str(t))
elif f - s == t:
    sys.stdout.write(str(f) + '-' + str(s) + '=' + str(t))
elif f * s == t:
    sys.stdout.write(str(f) + '*' + str(s) + '=' + str(t))
elif f / s == t:
    sys.stdout.write(str(f) + '/' + str(s) + '=' + str(t))
elif s + t == f:
    sys.stdout.write(str(f) + '=' + str(s) + '+' + str(t))
elif s - t == f:
    sys.stdout.write(str(f) + '=' + str(s) + '-' + str(t))
elif s * t == f:
    sys.stdout.write(str(f) + '=' + str(s) + '*' + str(t))
elif s / t == f:
    sys.stdout.write(str(f) + '=' + str(s) + '/' + str(t))
