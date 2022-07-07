# Field Trip
# Solution by Hasan Kalzi 15-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/fieldtrip
from sys import stdin, stdout

n = int(stdin.readline())
sections = [int(_) for _ in stdin.readline().split()]
sum_sections = sum(sections)
if sum_sections % 3 == 0:
    sum_bus = 0
    answer = []
    for i in range(n):
        if sum_bus == sum_sections / 3:
            answer.append(i)
            sum_bus = 0
        if sum_bus > sum_sections / 3:
            stdout.write('-1')
            break
        sum_bus += sections[i]
    if len(answer) == 2:
        stdout.write(str(answer[0]) + ' ' + str(answer[1]))
else:
    stdout.write('-1')
