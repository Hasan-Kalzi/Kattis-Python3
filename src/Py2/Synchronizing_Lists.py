# Synchronizing Lists
# Solution by Hasan Kalzi 23-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/synchronizinglists
from sys import stdin, stdout
while 1:
    n = int(stdin.readline())
    #  Input ends when n=0.
    if n == 0:
        break
    list1 = []
    list2 = []
    # fill the lists
    for i in range(n):
        list1.append(int(stdin.readline()))
    for i in range(n):
        list2.append(int(stdin.readline()))
    # a copy of list1 but sorted
    temp = sorted(list1)
    # sort list2
    list2.sort()

    # we try to find the position of the i element of list1 in temp
    # Because temp and list2 are sorted so the corresponding position will be the same
    for i in range(n):
        for j in range(n):
            if list1[i] == temp[j]:
                stdout.write(str(list2[j])+'\n')
                break
    stdout.write('\n')
