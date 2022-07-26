# Simon Says
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/simonsays
from sys import stdin, stdout
for _ in range(int(stdin.readline())):
    text = stdin.readline().strip()
    if "Simon says" in text:
        print(text[11:])
