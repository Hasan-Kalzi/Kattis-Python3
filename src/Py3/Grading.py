# Grading
# Solution by Hasan Kalzi 31-10-2021
# Link to problem in Kattis: https://open.kattis.com/problems/grading
from sys import stdin, stdout

a, b, c, d, e = map(int, stdin.readline().split())
grade = int(stdin.readline())
if grade >= a:
    stdout.write('A')
elif grade >= b:
    stdout.write('B')
elif grade >= c:
    stdout.write('C')
elif grade >= d:
    stdout.write('D')
elif grade >= e:
    stdout.write('E')
else:
    stdout.write('F')
