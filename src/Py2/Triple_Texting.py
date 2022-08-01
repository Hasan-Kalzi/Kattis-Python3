# Triple Texting
# # Solution by Hasan Kalzi 26-03-2021
# # Link to problem in https://open.kattis.com/problems/tripletexting
import sys

tri_word = sys.stdin.readline()
n = len(tri_word[0:len(tri_word) - 1]) // 3
answer = []
for i in range(n):
    x = [tri_word[i], tri_word[i + n], tri_word[i + n + n]]
    answer.append(sorted(x)[1])
sys.stdout.write(''.join(answer))
