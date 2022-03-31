# ACM Contest Scoring
# Solution by Hasan Kalzi 05-04-2021
# Link to problem i https://open.kattis.com/problems/acm
from sys import stdin, stdout

answers = {}
while 1:
    line = stdin.readline()
    if line == "-1\n":
        break
    else:
        m, problem, status = line.split()
        if problem not in answers:
            answers[problem] = [0, 0]
        if status == "wrong":
            answers[problem][0] += 20
        else:
            answers[problem][0] += int(m)
            answers[problem][1] = 1
score, right = 0, 0
for answer in answers:
    if answers[answer][1] == 1:
        right += 1
        score += answers[answer][0]
stdout.write(str(right) + ' ' + str(score))
