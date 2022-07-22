# coding=utf-8
# Ptice
# Solution by Hasan Kalzi 21-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/ptice
from sys import stdin, stdout
# All the necessary values
values = [["Adrian", "Bruno", "Goran"],
          [["A", "B", "C"] * 34, ["B", "A", "B", "C"] * 25, ["C", "C", "A", "A", "B", "B"] * 17], [0, 0, 0]]
# The first line contains an integer N (1≤N≤100), the number of questions on the exam.
number = int(stdin.readline())
given_string = stdin.readline()
# The first line contains an integer N (1≤N≤100), the number of questions on the exam.
# after range is the inserted values of N: int(sys.stdin.readline())
for i in range(number):
    if given_string[i] == values[1][0][i]:
        values[2][0] += 1
    if given_string[i] == values[1][1][i]:
        values[2][1] += 1
    if given_string[i] == values[1][2][i]:
        values[2][2] += 1
# output M, the largest number of correct answers one of the three boys gets.
stdout.write(str(max(values[2]))+"\n")
# output the names of the boys (in alphabetical order) whose sequences result in M correct answers.
if values[2][0] == values[2][1] and values[2][1] == values[2][2]:
    stdout.write("Adrian" + "\n" + "Bruno" + "\n" + "Goran")
elif values[2][0] == values[2][1] and values[2][2] < values[2][0]:
    stdout.write("Adrian" + "\n" + "Bruno")
elif values[2][0] == values[2][2] and values[2][1] < values[2][0]:
    stdout.write("Adrian" + "\n" + "Goran")
elif values[2][1] == values[2][2] and values[2][0] < values[2][1]:
    stdout.write("Bruno" + "\n" + "Goran")
else:
    stdout.write(values[0][values[2].index(max(values[2]))])
