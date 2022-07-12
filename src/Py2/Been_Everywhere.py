# I've Been Everywhere, Man
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/everywhere
from sys import stdin, stdout
for _ in range(int(stdin.readline())):
    cities = []
    for _ in range(int(stdin.readline())):
        city = stdin.readline().strip()
        if city not in cities:
            cities.append(city)
    stdout.write(str(len(cities))+'\n')
