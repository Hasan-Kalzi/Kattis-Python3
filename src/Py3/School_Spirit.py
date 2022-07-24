# School Spirit
# Solution by Hasan Kalzi 14-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/schoolspirit
import math
import sys


def one_leaves(member, group_scores):
    without_one = 0
    new_i = 0
    for j in range(len(group_scores)):
        if j == member:
            continue
        else:
            without_one += scores[j] * math.pow(4 / 5, new_i)
            new_i += 1
    return without_one / 5


if __name__ == '__main__':
    average = 0
    score = 0
    n = int(sys.stdin.readline())
    scores = []
    for i in range(n):
        scores.append(int(sys.stdin.readline()))
        score += scores[i] * math.pow(4 / 5, i)
    sys.stdout.write(str(score / 5) + "\n")
    for i in range(len(scores)):
        # recalculate the score without the member number i in the group
        average += one_leaves(i, scores)
    sys.stdout.write(str(average / len(scores)))
