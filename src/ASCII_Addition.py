# ASCII Addition
# Solution by Hasan Kalzi 25-06-2021
# Link to problem in Kattis: https://open.kattis.com/problems/asciiaddition
from sys import stdin, stdout

zero = "xxxxx\nx...x\nx...x\nx...x\nx...x\nx...x\nxxxxx"
one = "....x\n....x\n....x\n....x\n....x\n....x\n....x"
two = "xxxxx\n....x\n....x\nxxxxx\nx....\nx....\nxxxxx"
three = "xxxxx\n....x\n....x\nxxxxx\n....x\n....x\nxxxxx"
four = "x...x\nx...x\nx...x\nxxxxx\n....x\n....x\n....x"
five = "xxxxx\nx....\nx....\nxxxxx\n....x\n....x\nxxxxx"
six = "xxxxx\nx....\nx....\nxxxxx\nx...x\nx...x\nxxxxx"
seven = "xxxxx\n....x\n....x\n....x\n....x\n....x\n....x"
eight = "xxxxx\nx...x\nx...x\nxxxxx\nx...x\nx...x\nxxxxx"
nine = "xxxxx\nx...x\nx...x\nxxxxx\n....x\n....x\nxxxxx"
plus = ".....\n..x..\n..x..\nxxxxx\n..x..\n..x..\n....."
numbers = ["", ""]
operations = []
line = stdin.readline().strip()
x = int(len(line) / 6)
for i in range(x + 6):
    operations.append("")
    operations[i] += (line[(i * 6):(i * 6) + 5] + "\n")

for i in range(6):
    line = stdin.readline().strip()
    for k in range(x + 6):
        operations[k] += (line[(k * 6):(k * 6) + 5] + "\n")
switch = 0
for element in operations:
    if element.strip() == plus:
        switch = 1
    elif element.strip() == zero:
        numbers[switch] += "0"
    elif element.strip() == one:
        numbers[switch] += "1"
    elif element.strip() == two:
        numbers[switch] += "2"
    elif element.strip() == three:
        numbers[switch] += "3"
    elif element.strip() == four:
        numbers[switch] += "4"
    elif element.strip() == five:
        numbers[switch] += "5"
    elif element.strip() == six:
        numbers[switch] += "6"
    elif element.strip() == seven:
        numbers[switch] += "7"
    elif element.strip() == eight:
        numbers[switch] += "8"
    elif element.strip() == nine:
        numbers[switch] += "9"
answer = int(numbers[0]) + int(numbers[1])
output = ""

for i in range(7):
    k = 0
    for digit in str(answer):
        k += 1
        if digit == '0':
            output += zero[i * 6: (i * 6) + 6].strip()
        elif digit == '1':
            output += one[i * 6: (i * 6) + 6].strip()
        elif digit == '2':
            output += two[i * 6: (i * 6) + 6].strip()
        elif digit == '3':
            output += three[i * 6: (i * 6) + 6].strip()
        elif digit == '4':
            output += four[i * 6: (i * 6) + 6].strip()
        elif digit == '5':
            output += five[i * 6: (i * 6) + 6].strip()
        elif digit == '6':
            output += six[i * 6: (i * 6) + 6].strip()
        elif digit == '7':
            output += seven[i * 6: (i * 6) + 6].strip()
        elif digit == '8':
            output += eight[i * 6: (i * 6) + 6].strip()
        elif digit == '9':
            output += nine[i * 6: (i * 6) + 6].strip()
        if k != len(str(answer)):
            output += '.'
    if i != 6:
        output += "\n"

stdout.write(output)
