# coding=utf-8
# Kleptography
# Solution by Hasan Kalzi 21-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/kleptography
import string
from sys import stdin, stdout
alphabet = list(string.ascii_lowercase)
# One line with two integers n and m (1≤n≤30, n+1≤m≤100),
# where n is the length of the keyword as well as the number of letters Mary saw, and m is the length of the text.
n, m = map(int, stdin.readline().split())
# One line with n lower-case letters, the last n letters of the plaintext.
last = stdin.readline().strip()
# One line with m lower-case letters, the whole ciphertext.
cipher = stdin.readline().strip()
key = [1] * n
answer = last
for i in range(n):
    key[i] = ((alphabet.index(cipher[m - i - 1]) - alphabet.index(last[n - 1 - i])) % 26)
    answer = alphabet[key[i]] + answer
i = 0
m = m - n
j = 0
for _ in range(m , 0, -1):
    if i == n:
        i = 0
        m = m - n
    key[i] = (alphabet.index(cipher[m - i - 1]) - key[i]) % 26
    answer = alphabet[key[i]] + answer
    i += 1
stdout.write(answer[n:len(answer)])
