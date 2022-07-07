# Estimating the Area of a Circle
# Solution by Hasan Kalzi 25-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/estimatingtheareaofacircle
import sys

while True:
    # Input contains up to 1000 test cases, one test case per line. Each line has three space-separated numbers: r m c,
    # where 0<r≤1000 is a real number with at most 5 digits past the decimal indicating the true radius of the circle,
    # 1≤m≤100000 is an integer indicating the total number of marked points,
    # and 0≤c≤m is an integer indicating the number of marked points that fall in the circle.
    r, m, c = [float(_) for _ in sys.intern(sys.stdin.readline()).split()]
    # Input ends with a line containing three zeros, which should not be processed.
    if r == 0 and m == 0 and c == 0:
        break
    # For each test case, print a line containing two numbers: the true area of the circle and the estimate according to
    # the experiment. Both numbers may have a relative error of at most 10−5.
    sys.stdout.write(" ".join([str(3.141592653589793 * (r ** 2)), str((2 * r) * (2 * r) * (c / m)), '\n']))
