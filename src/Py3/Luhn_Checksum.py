# Luhn's Checksum Algorithm
# Solution by Hasan Kalzi 10-04-2021
# Link to problem in https://open.kattis.com/problems/luhnchecksum
from sys import stdin, stdout


def main():
    for _ in range(int(stdin.readline())):
        value = stdin.readline().strip()
        check_sum = 0
        double_value = 1
        for i in range(len(value) - 1, -1, -1):
            if double_value == 0:
                plus = 2 * int(value[i])
                if plus > 9:
                    plus = int(str(plus)[0]) + int(str(plus)[1])
                double_value += 1
                check_sum += plus
            else:
                check_sum += int(value[i])
                double_value -= 1
        if check_sum % 10 == 0:
            stdout.write("PASS\n")
        else:
            stdout.write('FAIL\n')


main()
