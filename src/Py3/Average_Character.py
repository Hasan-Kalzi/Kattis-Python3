# Average Character
# This program calculates the average ASCII value of the characters in a given input string
# Solution by Hasan Kalzi 14-03-2022
# Link to the problem in Kattis: https://open.kattis.com/problems/averagecharacter

# Importing standard input and output modules from sys package
from sys import stdin, stdout

# Initializing variables to store the sum of ASCII values and count of characters
ascii_sum = 0
count = 0

# Looping through each character in the input string
for char in stdin.readline().strip():
    # Adding the ASCII value of the character to the sum
    ascii_sum += ord(char)
    # Incrementing the count of characters
    count += 1

# Calculating the average ASCII value using integer division
average_ascii = ascii_sum // count

# Converting the average ASCII value to its corresponding character
average_char = chr(average_ascii)

# Writing the average character to the output stream
stdout.write(average_char)
