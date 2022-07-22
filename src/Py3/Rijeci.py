# Riječi
# Solution by Hasan Kalzi 18-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/rijeci
import sys

a = [0] * 46
b = [0] * 46
sum_a_b = [1] * 46
a[0] = 1
b[1] = 1
a[2] = 1
b[2] = 1
sum_a_b[2] = 2
# The first line of input contains the integer K (1≤K≤45), the number of times Mirko pressed the button.
k = int(sys.stdin.readline())
if k > 2:
    for i in range(3, k+1):  # K
        b[i] = sum_a_b[i-1]
        a[i] = sum_a_b[i-2]
        sum_a_b[i] = a[i] + b[i]
sys.stdout.write(str(a[k]) + " " + str(b[k]))
