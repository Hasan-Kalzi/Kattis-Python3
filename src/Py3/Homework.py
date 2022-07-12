# Homework
# Solution by Hasan Kalzi 18-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/heimavinna
import sys

homework = [_ for _ in sys.stdin.readline().split(";")]
number_of_homework = 0
for work in homework:
    if "-" in work:
        start, end = [int(_) for _ in work.split("-")]
        number_of_homework += (end - start) + 1
    else:
        number_of_homework += 1
sys.stdout.write(str(number_of_homework))
