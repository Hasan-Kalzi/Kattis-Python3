# Alphabet Spam
# Solution by Hasan Kalzi 23-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/alphabetspam

# Importing standard input and output library from sys module
from sys import stdin, stdout

# Read input from standard input and remove trailing newline
sentence = stdin.readline().rstrip()

# Initialize counters
num_chars = len(sentence)
num_white_space, num_small_alpha, num_big_alpha, num_symbols = 0, 0, 0, 0

# Iterate over each character in the sentence
for character in sentence:
    if character.islower():
        num_small_alpha += 1
    elif character.isupper():
        num_big_alpha += 1
    elif character == "_":
        num_white_space += 1
    else:
        num_symbols += 1

# Calculate ratios using divmod() and write to standard output
stdout.write("{:.15f}\n{:.15f}\n{:.15f}\n{:.15f}".format(*divmod(num_white_space, num_chars), *divmod(num_small_alpha, num_chars), *divmod(num_big_alpha, num_chars), *divmod(num_symbols, num_chars)))
