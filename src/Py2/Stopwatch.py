# Stopwatch
# # Solution by Hasan Kalzi 29-03-2021
# # Link to problem in https://open.kattis.com/problems/stopwatch
import sys

number_pressed = int(sys.stdin.readline())
if number_pressed % 2 != 0:
    sys.stdout.write("still running")
else:
    displayed = 0
    for _ in range(int(number_pressed / 2)):
        displayed += abs(int(sys.stdin.readline()) - int(sys.stdin.readline()))
    sys.stdout.write(str(displayed))
