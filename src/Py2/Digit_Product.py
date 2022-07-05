# Digit Product
# Solution by Hasan Kalzi 24-03-2021
# Link to problem in https://open.kattis.com/problems/sifferprodukt
from sys import stdin, stdout


def calc(string_number, answer):
    for char in string_number:
        if char != '0':
            answer *= int(char)
    return int(answer)


number = stdin.readline()
result = calc(number[0:len(number)-1], 1)
while result > 9:
    result = calc(str(result), 1)
stdout.write(str(result))
