# Janitor Troubles
# Solution by Hasan Kalzi 18-12-2020
# Link to problem i Kattis: https://open.kattis.com/problems/janitortroubles
import math
import sys

# The input consists of a single line with four positive integers, the four side lengths s1, s2, s3, and s4.
s1, s2, s3, s4 = [int(_) for _ in sys.stdin.readline().split()]
semi_perimeter = (s1 + s2 + s3 + s4) / 2
sys.stdout.write(str(math.sqrt((semi_perimeter - s1) * (semi_perimeter - s2)
                               * (semi_perimeter - s3) * (semi_perimeter - s4))))
