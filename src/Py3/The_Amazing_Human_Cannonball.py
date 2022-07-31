# The Amazing Human Cannonball
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/humancannonball2

import math

number_of_tests_N = int(input())  # The number of cases we want to check

# Check for every test case
for _ in range(number_of_tests_N):
    values = [float(x) for x in input().split()]  # Saving v0, theta , x1 , h1, h2 in list in given order
    # values[0] = v0 , values[1] = theta, values[2] = x1, values[3] = h1, values[4] = h2
    # t =  X(t)/ v0.cos(theta) theta in radians
    t = values[2] / (math.cos(math.radians(values[1])) * values[0])
    # Y(t) = v0*t*sin(theta) * t - 0.5 * g * t^2 : g = 9.81 m/s^2
    y1 = (values[0] * t * math.sin(math.radians(values[1]))) - (0.5 * 9.81 * t * t)
    # To pass safely, there has to be a vertical safety margin of 1 m both below and above the point where the ball’s
    # trajectory crosses the center line of the wall
    if y1 - values[3] < 1:  # must y1 - h1 > 1
        print("Not Safe")
    elif values[4] - y1 < 1:  # must h2 - y1 > 1
        print("Not Safe")
    else:
        print("Safe")
