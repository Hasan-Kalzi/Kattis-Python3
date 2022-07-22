# Quick Brown Fox
# Solution by Hasan Kalzi 15-01-2021
# Link to problem in Kattis: https://open.kattis.com/problems/quickbrownfox
from sys import stdin, stdout

missing = 0
letters = [0] * 26
for i in range(int(stdin.readline())):
    phrase = stdin.readline()
    for char in phrase:
        if 96 < ord(char) < 123:
            letters[ord(char) - 97] += 1
        elif 64 < ord(char) < 91:
            letters[ord(char) - 65] += 1
    for j in range(26):
        if letters[j] == 0 and missing == 0:
            stdout.write("missing " + chr(j + 97))
            missing = 1
        elif letters[j] == 0:
            stdout.write(chr(j + 97))
    if missing == 0:
        stdout.write('pangram')
    stdout.write('\n')
    letters = [0] * 26
    missing = 0
