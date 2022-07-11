# Hangman
# Solution by Hasan Kalzi 24-03-2021
# Link to problem in https://open.kattis.com/problems/hangman
import sys

word = sys.stdin.readline()
guess = sys.stdin.readline()
lose = 0
for char in guess:
    if char in word:
        word = word.replace(char, '')
    else:
        lose += 1
    if len(word) == 1:
        sys.stdout.write("WIN")
        break
    if lose == 10:
        sys.stdout.write("LOSE")
        break
