# Encoded Message
# Solution by Hasan Kalzi 22-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/encodedmessage
from sys import stdin, stdout
import math
# after range is the inserted number of events of words: int(input())
for _ in range(int(stdin.readline())):
    # The decoded word
    decoded_word = ""
    # The inserted word in row i
    word_i = stdin.readline().strip()
    # Because it is square
    sqrt_length = math.sqrt(len(word_i))
    matrix = [[0 for _ in range(int(sqrt_length))] for _ in range(int(sqrt_length))]
    temp = int(sqrt_length)
    # This operation to fill a 90 degrees rotated matrix av sequence number matrix
    # for example this will result rotation of [[0,1,2],[3,4,5],[6,7,8]]
    # which equals [[2,5,8],[1,4,7],[0,3,6]]
    for i in range(int(sqrt_length)):
        n = 0
        for j in range(int(sqrt_length)):
            matrix[i][j] = temp - 1 + n
            n += int(sqrt_length)
        temp -= 1
    # Rebuild the decoded word again
    for i in range(int(sqrt_length)):
        for j in range(int(sqrt_length)):
            decoded_word += word_i[matrix[i][j]]
    stdout.write(str(decoded_word)+'\n')
