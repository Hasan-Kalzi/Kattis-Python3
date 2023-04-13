# A Real Challenge
# Solution by Hasan Kalzi 26-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/areal

# Importing modules
from sys import stdin, stdout
from math import sqrt

# Reading input from standard input (stdin), parsing it as an integer and calculating the area
#  of a square with side length x is equal to x^2
# Taking the square root of that area gives us the length of the diagonal
# Multiplying that length by 4 gives us the perimeter of the square
stdout.write(str(4 * sqrt(int(stdin.readline()))))
