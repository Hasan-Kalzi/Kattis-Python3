# Apaxiaaaaaaaaaaaans!
# Solution by Hasan Kalzi 11-03-2021
# Link to problem i https://open.kattis.com/problems/apaxiaaans
import sys

word = sys.stdin.readline()
prev_char = word[0]
right_form = word[0]
for letter in word[1:]:
    if letter != prev_char:
        right_form += letter
    prev_char = letter
sys.stdout.write(right_form)
