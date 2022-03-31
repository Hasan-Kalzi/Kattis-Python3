# Alphabet Spam
# Solution by Hasan Kalzi 23-10-2020
# Link to problem i Kattis: https://open.kattis.com/problems/alphabetspam
import io
import os
import sys

white_space = 0
small_alpha = 0
big_alpha = 0
symbols = 0
sentence = sys.stdin.readline().replace('\n', '')
for character in sentence:
    if character.islower():
        small_alpha += 1
    elif character.isupper():
        big_alpha += 1
    elif character == "_":
        white_space += 1
    else:
        symbols += 1
sys.stdout.write(str(float(white_space) / len(sentence)) + '\n' + str(float(small_alpha )/ len(sentence))
                 + '\n' + str(float(big_alpha) / len(sentence)) + '\n' + str(float(symbols) / len(sentence)))
