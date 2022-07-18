# Number Fun
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/numberfun

number_of_tests = int(input())
for _ in range(number_of_tests):
    first, second, third = [int(x) for x in input().split()]
    if first + second == third:
        print("Possible")
    elif first * second == third:
        print("Possible")
    elif first - second == third or second - first == third:
        print("Possible")
    elif first / second == third or second / first == third:
        print("Possible")
    else:
        print("Impossible")
