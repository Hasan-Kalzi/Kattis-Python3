# Star Arrangements
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/stararrangements
from sys import stdin, stdout


def check_numbers(stars_1, stars_2):
    test = 0
    i = 1
    j = 1
    while test < int(number_of_stars):
        test = stars_1 * i + stars_2 * j
        if i > j:
            j += 1
        else:
            i += 1
        if test == int(number_of_stars):
            stdout.write(str(stars_1) + "," + str(stars_2)+'\n')
            break


number_of_stars = stdin.readline().strip()
stdout.write(number_of_stars + ":\n")
for stars_in_line_1 in range(2, int(number_of_stars) + 1):
    stars_in_line_2 = stars_in_line_1 - 1
    check_numbers(stars_in_line_1, stars_in_line_2)
    stars_in_line_2 += 1
    check_numbers(stars_in_line_1, stars_in_line_2)
