# Arrangement
# Solution by Hasan Kalzi 11-03-2021
# Link to problem i Kattis: https://open.kattis.com/problems/upprodun
# Importing the necessary modules for input/output operations.
from sys import stdout,stdin

# On the first line is an integer N, and on the second line is an integer M.
n = int(stdin.readline())
m = int(stdin.readline())

# Initializing complementary to 0 and checking whether M is divisible by N.
complementary = m % n
m -= complementary

while n > 0:
    # Calculate the number of asterisks to print
    asterisks = '*' * (m // n)
    if complementary > 0:
        asterisks += '*'
        complementary -= 1
    # Print the line of asterisks
    stdout.write('{}\n'.format(asterisks))
    n -= 1

