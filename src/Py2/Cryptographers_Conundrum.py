# Cryptographer's Conundrum
# Solution by Hasan Kalzi 22-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/conundrum
from sys import stdin, stdout
cipher_text = stdin.readline().strip().upper()
number_of_days = 0
for i in range(int(len(cipher_text) / 3)):
    if cipher_text[i*3] != "P":
        number_of_days += 1
    if cipher_text[1+(i*3)] != "E":
        number_of_days += 1
    if cipher_text[2+(i*3)] != "R":
        number_of_days += 1
stdout.write(str(number_of_days))
