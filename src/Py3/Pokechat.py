# Pokechat
# Solution by Hasan Kalzi 18-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/pokechat
from sys import stdin, stdout

message, code = stdin.readline().strip(), stdin.readline().strip()
for i in range(0, len(code), 3):
    stdout.write(message[int(code[i:i + 3]) - 1])
