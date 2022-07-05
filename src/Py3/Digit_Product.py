# Digit Product
# Solution by Hasan Kalzi 24-03-2021
# Link to problem i https://open.kattis.com/problems/sifferprodukt
import sys


def calc(string_number, answer):
    for char in string_number:
        if char != '0':
            answer *= int(char)
    return int(answer)


number = sys.stdin.readline()
result = calc(number[0:len(number)-1], 1)
while result > 9:
    result = calc(str(result), 1)
sys.stdout.write(str(result))
