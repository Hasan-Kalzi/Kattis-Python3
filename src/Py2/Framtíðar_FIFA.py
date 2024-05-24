# Framtíðar FIFA
# Solution by Hasan Kalzi 24-05-2024
# Link to the problem in Kattis: https://open.kattis.com/problems/fifa

from __future__ import division
from sys import stdout, stdin


improvements = int(stdin.readline())
number_of_improvements_year = int(stdin.readline())

if improvements % number_of_improvements_year != 0:
    stdout.write(str(int(improvements / number_of_improvements_year)+2023))
else:
    stdout.write(str(int(improvements / number_of_improvements_year) + 2022))
