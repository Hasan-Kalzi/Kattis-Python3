# Roaming Romans
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/romans
from __future__ import division
from sys import stdin, stdout

english_miles = float(stdin.readline())
# calculating the inserted english miles in roman paces.
roman_paces = (english_miles * 1000 * 5280) / 4854
# printing the rounded result.
stdout.write(str(int(round(roman_paces))))
