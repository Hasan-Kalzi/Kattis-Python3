# Course Scheduling
# Solution by Hasan Kalzi 25-06-2021
# Link to problem in Kattis: https://open.kattis.com/problems/coursescheduling
from sys import stdin, stdout

courses = []
names = []
for _ in range(int(stdin.readline())):
    first, last, course = stdin.readline().strip().split()
    if course not in courses:
        courses.append(course)
        names.append([])
    name = first + " " + last
    i = courses.index(course)
    if name not in names[i]:
        names[i].append(name)
answer = []
for c in courses:
    answer.append([c, str(len(names[courses.index(c)]))])
answer = sorted(answer, key=lambda x: x[0])
for ans in answer:
    stdout.write(ans[0] + ' ' + ans[1] + '\n')
