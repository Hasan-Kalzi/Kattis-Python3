# Filip
# Solution by Hasan Kalzi 22-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/filip

def reverse_number(n):
    reversed_number = 0
    while n != 0:
        r = int(n % 10)
        reversed_number = reversed_number * 10 + r
        n = int(n / 10)
    return reversed_number


values = [int(x) for x in input().split()]
x = reverse_number(values[0])
y = reverse_number(values[1])
if x > y:
    print(x)
else:
    print(y)
