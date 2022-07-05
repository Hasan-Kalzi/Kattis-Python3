# coding=utf-8
# Drunk Vigenère
# Solution by Hasan Kalzi 25-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/drunkvigenere
import sys

encrypt, key = sys.stdin.readline(), sys.stdin.readline()
for i in range(len(encrypt) - 1):
    if key[i] is chr(65):
        sys.stdout.write(encrypt[i])
    elif i % 2 == 0:
        sys.stdout.write(chr((ord(encrypt[i]) - 65 - ord(key[i]) - 65) % 26+65))
    else:
        sys.stdout.write(chr((ord(encrypt[i]) - 65 + ord(key[i]) - 65) % 26+65))
