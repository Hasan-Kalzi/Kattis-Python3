# Arm Coordination
# Solution by Hasan Kalzi 06-12-2021
# Link to the problem in Kattis: https://open.kattis.com/problems/armcoordination

# Importing the necessary function(s) from the sys module
from sys import stdin, stdout

# Reading input values from standard input and storing them in variables
x, y = map(int, stdin.readline().split())  # The first line contains two integers separated by a space
r = int(stdin.readline())  # The second line contains an integer

# Printing the output to standard output using formatted string literals
stdout.write(f"{x + r} {y + r}\n{x + r} {y - r}\n{x - r} {y - r}\n{x - r} {y + r}\n")
