# T9 Spelling
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/t9spelling
import sys

current_btn = 1
for i in range(1,int(sys.stdin.readline())+1):
    sys.stdout.write("Case #" + str(i) + ": ")
    for char in sys.stdin.readline():
        if char in "abc":
            if current_btn == 2:
                sys.stdout.write(' ')
            sys.stdout.write('2' * "2abc".index(char))
            current_btn = 2
        elif char in "def":
            if current_btn == 3:
                sys.stdout.write(' ')
            sys.stdout.write('3' * "3def".index(char))
            current_btn = 3
        elif char in "ghi":
            if current_btn == 4:
                sys.stdout.write(' ')
            sys.stdout.write('4' * "4ghi".index(char))
            current_btn = 4
        elif char in "jkl":
            if current_btn == 5:
                sys.stdout.write(' ')
            sys.stdout.write('5' * "5jkl".index(char))
            current_btn = 5
        elif char in "mno":
            if current_btn == 6:
                sys.stdout.write(' ')
            sys.stdout.write('6' * "6mno".index(char))
            current_btn = 6
        elif char in "pqrs":
            if current_btn == 7:
                sys.stdout.write(' ')
            sys.stdout.write('7' * "7pqrs".index(char))
            current_btn = 7
        elif char in "tuv":
            if current_btn == 8:
                sys.stdout.write(' ')
            sys.stdout.write('8' * "8tuv".index(char))
            current_btn = 8
        elif char in "wxyz":
            if current_btn == 9:
                sys.stdout.write(' ')
            sys.stdout.write('9' * "9wxyz".index(char))
            current_btn = 9
        elif char == '\n':
            sys.stdout.write('\n')
        elif char == ' ':
            if current_btn == 0:
                sys.stdout.write(' ')
            sys.stdout.write('0')
            current_btn = 0
    current_btn = 1
