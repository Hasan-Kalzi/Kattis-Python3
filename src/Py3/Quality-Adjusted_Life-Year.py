# Quality-Adjusted Life-Year
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/qaly


result = 0
# after range is the inserted number of lines: int(input())
for _ in range(int(input())):
    q, y = [float(x) for x in input().split()]
    result += q * y
print(result)
