# Count the Vowels
# Solution by Hasan Kalzi 14-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/countthevowels
from sys import stdin, stdout

sentence, count = stdin.readline().strip(), 0
for i in range(len(sentence)):
    char = sentence[i].lower()
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
stdout.write(str(count))
