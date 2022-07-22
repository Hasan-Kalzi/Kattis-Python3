# Quality-Adjusted Life-Year
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/qaly
from sys import stdin, stdout

result = 0
# after range is the inserted number of lines: int(input())
for _ in range(int(stdin.readline())):
    q, y = map(float, stdin.readline().split())
    result += q * y
stdout.write(str(result))
