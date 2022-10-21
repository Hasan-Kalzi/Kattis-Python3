# Haughty Cuisine
# Solution by Hasan Kalzi 21-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/haughtycuisine
from sys import stdin, stdout

for _ in range(int(stdin.readline())-1):
    stdin.readline()
for dishes in stdin.readline().split():
    stdout.write(dishes+'\n')

