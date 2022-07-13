# Jazz it Up!
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/jazzitup
from sys import stdin, stdout


def calc_m(number, sqr_list):
    len_list = len(sqr_list) - 1
    for i in range(2, number):
        k = number * i
        for j in range(number - 2):
            if k % sqr_list[j] == 0:
                break
            if j == len_list:
                stdout.write(str(i) + '\n')
                return


n = int(stdin.readline())

numbers = [_ ** 2 if _ <= n ** 2 else 0 for _ in range(2, n)]

calc_m(n, numbers)
