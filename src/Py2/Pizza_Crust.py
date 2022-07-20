# Pizza Crust
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/pizza2
from __future__ import division
import math
import sys

r, c = map(int, sys.stdin.readline().split())
sys.stdout.write(str(((math.pi * (r - c) * (r - c) * 4) / (math.pi * r * r * 4)) * 100))
