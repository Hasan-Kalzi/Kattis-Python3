# 99 Problems
# Solution by Hasan Kalzi 17-05-2022
# Link to problem in https://open.kattis.com/problems/99problems

# Import the standard input and output streams from sys module
from sys import stdin, stdout

# Read the input number as a string from standard input and remove any leading/trailing whitespaces
number = stdin.readline().strip()

# Check if the length of the number is between 1 and 2 (inclusive)
if 1 <= len(number) <= 2:
    # If so, the answer is 99 (always)
    stdout.write("99")
# Check if the last two digits of the number are both 9
elif number[-1] == '9' and number[-2] == '9':
    # If so, the answer is the number itself
    stdout.write(number)
else:
    # Otherwise, find the smallest and largest 2-digit numbers that end with 9
    bigger = int(number[:-2] + '99')   # The largest number
    smaller = int(str(int(number[:-2]) - 1) + '99')  # The smallest number

    # Check if the difference between the largest number and the input number is less than or equal to
    # the difference between the input number and the smallest number
    if bigger - int(number) <= int(number) - smaller:
        # If so, the answer is the largest number
        stdout.write(str(bigger))
    else:
        # Otherwise, the answer is the smallest number
        stdout.write(str(smaller))
