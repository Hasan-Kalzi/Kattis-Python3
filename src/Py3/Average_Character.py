# Average Character
# Solution by Hasan Kalzi 14-03-2022
# Link to the problem in Kattis: https://open.kattis.com/problems/averagecharacter
from sys import stdin, stdout

ints = [ord(_) for _ in [char for char in stdin.readline()][:-1]]

stdout.write(chr(int(sum(ints)/len(ints))))

