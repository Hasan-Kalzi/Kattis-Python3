# Calculating Dart Scores
# Solution by Hasan Kalzi 16-02-2022
# Link to problem in Kattis https://open.kattis.com/problems/calculatingdartscores
from __future__ import division
from sys import stdin, stdout


position = 0
answers = ['', '', '']
values = ["", "single ", "double ", "triple "]
impossible = 0
score = int(stdin.readline())
if 160 < score <= 180:
    if (score - 120) % 3 == 0:
        answers[position] = values[3] + str(int((score - 120) / 3))
        score = 120
        position += 1

    else:
        impossible = 1
        stdout.write("impossible")

if 140 < score <= 160 and impossible == 0:
    if (score - 120) % 3 == 0:
        answers[position] = values[3] + str(int((score - 120) / 3))
        score = 120
        position += 1
    elif (score - 120) % 2 == 0:
        answers[position] = values[2] + str(int((score - 120) / 2))
        score = 120
        position += 1
    else:
        score = score - 100
        if (score - 120) % 3 == 0:
            answers[position] = values[3] + str(int(score / 3))
            score = 100
            position += 1
        elif (score - 120) % 2 == 0:
            answers[position] = values[2] + str(int(score / 2))
            score = 100
            position += 1
        else:
            stdout.write("impossible")
            impossible = 1

if impossible == 0:
    if 120 < score <= 140:
        answers[position] = values[1] + str(int((score - 120)))
        score = score - (score - 120)
        position += 1

    if 100 <= score <= 120:
        answers[position] = values[3] + "20"
        score = score - 60
        position += 1
    if 80 <= score <= 100:
        answers[position] = values[3] + "20"
        score = score - 60
        position += 1

    if 60 <= score <= 80:
        answers[position] = values[3] + "20"
        score = score - 60
        position += 1
    if 40 <= score <= 60:
        answers[position] = values[2] + "20"
        score = score - 40
        position += 1
    if 20 <= score <= 40:
        answers[position] = values[1] + "20"
        score = score - 20
        position += 1

    if 0 < score <= 20:
        answers[position] = values[1] + str(score)

    for answer in answers:
        if answer != '':
            stdout.write(answer + '\n')
