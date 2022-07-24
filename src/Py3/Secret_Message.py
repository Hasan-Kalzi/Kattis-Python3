# Secret Message
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/secretmessage
import sys

for _ in range(int(sys.stdin.readline())):
    word = sys.stdin.readline()
    i = 1
    while (i * i) < len(word) - 1:
        i += 1
    new_word = word[:len(word) - 1] + ''.join('*' * ((i * i) - (len(word) - 1)))
    for j in range(i):
        for k in range(((i * i) - i) + j, j-1, -i):
            if new_word[k] == '*':
                continue
            else:
                sys.stdout.write(new_word[k])
    sys.stdout.write('\n')
