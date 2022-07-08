# FizzBuzz
# Solution by Hasan Kalzi 08-10-2020
# Link to problem i Kattis: https://open.kattis.com/problems/fizzbuzz

values = [int(x) for x in input().split()]
for i in range(1, values[2] + 1):
    if i % values[0] == 0 and i % values[1] == 0:
        print("FizzBuzz")
    elif i % values[0] == 0:
        print("Fizz")
    elif i % values[1] == 0:
        print("Buzz")
    else:
        print(i)
