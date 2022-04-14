# Birthday Memorization
# Solution by Hasan Kalzi 11-03-2021
# Link to the problem in Kattis: https://open.kattis.com/problems/fodelsedagsmemorisering/en
from sys import stdin, stdout


class Birthday:
    def __init__(self, birthday_list):
        self.person_name = birthday_list[0]
        self.priority = int(birthday_list[1])
        self.date = birthday_list[2]


birthdays = []
compared = []
willGo = []
for _ in range(int(stdin.readline())):
    birthdays.append(Birthday(stdin.readline().strip().split()))
    compared.append(0)

for i in range(len(birthdays)):
    temp = birthdays[i].person_name
    for j in range(i + 1, len(birthdays)):
        if compared[i] == 0:
            if birthdays[i].date == birthdays[j].date:
                if birthdays[i].priority < birthdays[j].priority:
                    compared[i] = 1
                    break
                else:
                    compared[j] = 1
    if compared[i] == 0:
        willGo.append(temp)

stdout.write(str(len(willGo)) + '\n')
for b in sorted(willGo):
    stdout.write(b + '\n')
