# Reversed Binary Numbers
# Solution by Hasan Kalzi 14-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/reversebinary
from __future__ import division
from sys import stdin, stdout


def reversed_binary_to_decimal(binary):
    decimal, i, n = 0, len(str(binary))-1, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i -= 1
    return decimal


if __name__ == '__main__':
    # takes the inserted decimal number and change it to binary and reverse it
    stdout.write(str(reversed_binary_to_decimal(int(bin(int(stdin.readline())).replace("0b", "")))))
