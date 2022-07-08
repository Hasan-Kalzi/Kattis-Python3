# Final Exam
# Solution by Hasan Kalzi 18-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/finalexam2
import sys

# The first line of the input contains a single integer n (1≤n≤1000) — the number of questions.
n = int(sys.intern(sys.stdin.readline()))
if n < 2:
    sys.stdout.write('0')
else:
    score = 0
    before, current = sys.intern(sys.stdin.readline()), sys.intern(sys.stdin.readline())
    if current is before:
        score += 1
    for _ in range(n - 2):
        current, before = sys.intern(sys.stdin.readline()), current
        if current is before:
            score += 1
    sys.stdout.write(str(score))
