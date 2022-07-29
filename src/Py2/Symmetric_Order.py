# coding=utf-8
# Symmetric Order
# Solution by Hasan Kalzi 14-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/symmetricorder
from sys import stdin, stdout

set_number = 1
while 1:
    list_of_names = []
    # after range is the inserted number of names of every set: int(sys.stdin.readline())
    number_of_names = int(stdin.readline())
    if number_of_names == 0:
        break
    # For each input set print “SET n” on a line, where n starts at 1.
    stdout.write("SET " + str(set_number) + "\n")
    # Save the names in the set in the list
    for i in range(number_of_names):
        list_of_names.append(stdin.readline())
    # print out the names in the desired order.
    for i in range(0, len(list_of_names), 2):
        stdout.write(list_of_names[i])
    # if the number of names in the set is even number
    if len(list_of_names) % 2 == 0:
        for i in range(len(list_of_names) - 1, 0, -2):
            stdout.write(list_of_names[i])
    # if the number of names in the set is odd number
    else:
        for i in range(len(list_of_names) - 2, 0, -2):
            stdout.write(list_of_names[i])
    set_number += 1
