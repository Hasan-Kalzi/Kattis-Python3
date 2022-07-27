# Spelling Bee
# Solution by Hasan Kalzi 11-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/spellingbee
import sys

testCase = sys.stdin.readline()
firstLetter = testCase[0]
for _ in range(int(sys.stdin.readline())):
    word = sys.stdin.readline()
    if firstLetter in word and len(word)-1 >= 4:
        for i in range(len(word)-1):
            x = testCase[:len(testCase)-1]
            if word[i] not in testCase[:len(testCase)-1]:
                break
            if i == len(word) - 2:
                sys.stdout.write(word)
