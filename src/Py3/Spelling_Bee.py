# Spelling Bee
# Solution by Hasan Kalzi 11-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/spellingbee

# Importing the sys module to read input from standard input
import sys

# Reading the first line of input to get the test case string
testCase = sys.stdin.readline()

# Extracting the first letter from the test case string
firstLetter = testCase[0]

# Looping over the remaining lines of input
for _ in range(int(sys.stdin.readline())):
    # Reading the next word from standard input
    word = sys.stdin.readline()

    # Checking if the first letter is in the word and if the word has at least 5 letters (excluding the newline character)
    if firstLetter in word and len(word)-1 >= 4:
        # Looping over the letters in the word (excluding the newline character)
        for i in range(len(word)-1):
            # Checking if the current letter is in the test case string
            if word[i] not in testCase[:len(testCase)]:
                # If the current letter is not in the test case string, break out of the loop
                break
            # If we reach the end of the word and all its letters are in the test case string, print the word
            if i == len(word) - 2:
                sys.stdout.write(word)