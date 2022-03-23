# Apaxiaaaaaaaaaaaans!
# Solution by Hasan Kalzi 11-03-2021
# Link to problem in Kattis https://open.kattis.com/problems/apaxiaaans
from sys import stdin, stdout

word = stdin.readline()
prev_char = word[0]
right_form = word[0]
for letter in word[1:]:
    if letter != prev_char:
        right_form += letter
    prev_char = letter
stdout.write(right_form)
