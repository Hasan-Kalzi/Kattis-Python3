# Musical Trees
# Solution by Hasan Kalzi 21-03-2021
# Link to problem in https://open.kattis.com/problems/musicaltrees
import sys

n, m = map(int, sys.stdin.readline().split())
people = sorted([int(_) for _ in sys.stdin.readline().split()])
trees = sorted([int(_) for _ in sys.stdin.readline().split()])
will_get = []
for i in range(n):
    min_distance = sys.maxint
    tree = -1
    for j in range(m):
        temp = abs(people[i] - trees[j])
        if temp < min_distance:
            tree = trees[j]
            min_distance = temp
        elif temp > min_distance:
            break
    if tree > -1:
        will_get.append(tree)
will_get = list(dict.fromkeys(will_get))
sys.stdout.write(str(n-len(will_get)))
