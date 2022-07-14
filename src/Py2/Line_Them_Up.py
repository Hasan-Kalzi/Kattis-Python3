# Line Them Up
# Solution by Hasan Kalzi 21-03-2021
# Link to problem in https://open.kattis.com/problems/lineup
import sys

names = []
for _ in range(int(sys.stdin.readline())):
    names.append(sys.stdin.readline())

if names == sorted(names):
    sys.stdout.write("INCREASING")
elif names == sorted(names, reverse=True):
    sys.stdout.write("DECREASING")
else:
    sys.stdout.write("NEITHER")
