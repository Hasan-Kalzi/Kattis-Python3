# Apaxiaaaaaaaaaaaans!
# Solution by Hasan Kalzi 11-03-2021
# Link to problem in Kattis https://open.kattis.com/problems/apaxiaaans

# Importing the stdin and stdout modules from sys
from sys import stdin, stdout

# Reading a single line of input from stdin and storing it in the variable 'word'
word = stdin.readline().rstrip()

# Initializing variables for the previous character and the correct form of the word
prev_char = word[0]
right_form = []

# Iterating through each character in the word, starting from the second character
for letter in word[1:]:
    # If the current character is not the same as the previous character, add it to the correct form
    if letter != prev_char:
        right_form.append(letter)
    # Set the previous character to the current character for the next iteration
    prev_char = letter

# Writing the correct form of the word to stdout
stdout.write("".join(right_form))
