# Haughty Cuisine
# Solution by Hasan Kalzi 21-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/haughtycuisine
import random
from sys import stdin, stdout

menus = []
for _ in range(int(stdin.readline())):
    menus.append(stdin.readline().split())
for dishes in menus[random.randint(0, len(menus)-1)]:
    stdout.write(dishes + '\n')
