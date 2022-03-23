# Alphabet Spam
# Solution by Hasan Kalzi 23-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/alphabetspam
from sys import stdin, stdout

white_space = 0
small_alpha = 0
big_alpha = 0
symbols = 0
sentence = stdin.readline().replace('\n', '')
for character in sentence:
    if character.islower():
        small_alpha += 1
    elif character.isupper():
        big_alpha += 1
    elif character == "_":
        white_space += 1
    else:
        symbols += 1
stdout.write(str(white_space / len(sentence)) + '\n' + str(small_alpha / len(sentence))
                 + '\n' + str(big_alpha / len(sentence)) + '\n' + str(symbols / len(sentence)))
