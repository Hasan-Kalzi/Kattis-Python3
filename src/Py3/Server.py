# Server
# Solution by Hasan Kalzi 15-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/server
from sys import stdin, stdout

n, t = map(int, stdin.readline().split())
tasks = [int(_) for _ in stdin.readline().split()]
current, counter = 0, 0
if sum(tasks) <= t:
    stdout.write(str(n))
else:
    for task in tasks:
        if task + current > t:
            break
        current += task
        counter += 1
    stdout.write(str(counter))
