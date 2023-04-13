# Add Two Numbers
# Solution by Hasan Kalzi 21-06-2021

# Import the sys module to read from standard input and write to standard output
from sys import stdin, stdout

# Read a line of input from standard input and split it into two integers
# The map function applies the int function to each element in the input line
# The sum function then adds the two integers together
result = sum(map(int, stdin.readline().split()))

# Write the result to standard output
stdout.write(str(result))
