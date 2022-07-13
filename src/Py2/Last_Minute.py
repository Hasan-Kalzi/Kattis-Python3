# Last Minute
# Solution by Hasan Kalzi 06-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/lastminute
from sys import stdin, stdout

au, bu, ar, br = map(int, stdin.readline().split())
if ar == 0 and br == 0:
    stdout.write(str(min(au, bu)))
elif br == 0:
    stdout.write(str(bu))
elif ar == 0:
    stdout.write(str(au))
else:
    stdout.write(str(au + bu + (ar * br)))
