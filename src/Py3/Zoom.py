# Zoom
# Solution by Hasan Kalzi 24-03-2022
# Link to problem in Kattis https://open.kattis.com/problems/apaxiaaans
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
zoom_numbers = stdin.readline().split()
for i in range(k - 1, n, k):
    stdout.write(zoom_numbers[i]+' ')
