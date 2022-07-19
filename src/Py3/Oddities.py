# Oddities
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/oddities

# after range is the inserted number of tests: int(input())
for _ in range(int(input())):
    number = int(input())
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
