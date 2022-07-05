# DRM Messages
# Solution by Hasan Kalzi 25-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/drmmessages
from __future__ import division
from sys import stdin, stdout, intern

first_half = 0
second_half = 0
first_word = []
second_word = []
encrypted = intern(stdin.readline())
for i in range(len(encrypted) - 1):
    if i < (len(encrypted) - 1) / 2:
        first_half += ord(encrypted[i]) - 65
    else:
        second_half += ord(encrypted[i]) - 65
for i in range(len(encrypted) - 1):
    if i < (len(encrypted) - 1) / 2:
        first_word.append((ord(encrypted[i]) - 65 + first_half) % 26)
    else:
        second_word.append((ord(encrypted[i]) - 65 + second_half) % 26)
for i in range(len(first_word)):
    stdout.write(chr((first_word[i] + second_word[i]) % 26 + 65))
