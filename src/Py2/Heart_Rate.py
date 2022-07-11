# Heart Rate
# Solution by Hasan Kalzi 08-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/heartrate
from __future__ import division
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    b, p = map(float, stdin.readline().split())
    bpm = (60 * b) / p
    stdout.write("%.4f" % (bpm - (60 / p)) + " " + "%.4f" % bpm + " " + "%.4f" % (bpm + (60 / p))+'\n')
