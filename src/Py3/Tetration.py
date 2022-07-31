# Tetration
# Solution by Hasan Kalzi 18-03-2021
# Link to problem in https://open.kattis.com/problems/tetration
import sys

n = float(sys.stdin.readline())
sys.stdout.write(str(n ** (1 / n)))
