# Birthday Memorization
# Solution by Hasan Kalzi 11-03-2021
# Link to the problem in Kattis: https://open.kattis.com/problems/fodelsedagsmemorisering/en
import sys


class Birthday:
    def __init__(self, person_name, priority, date):
        self.person_name = person_name
        self.priority = priority
        self.date = date


birthdays = []
willGo = []
ignore_list = []
temp = ''
same_date = False
for _ in range(int(sys.stdin.readline())):
    b_name, b_priority, b_date = sys.stdin.readline().split()
    birthdays.append(Birthday(b_name, b_priority, b_date))

for i in range(len(birthdays)):
    for j in range(len(birthdays)):
        if i not in ignore_list:
            if i != j and j not in ignore_list:
                if birthdays[i].date == birthdays[j].date:
                    same_date = True
                    if int(birthdays[i].priority) > int(birthdays[j].priority):
                        temp = birthdays[i].person_name
                        ignore_list.append(j)
                    else:
                        temp = ''
        else:
            break
    if i not in ignore_list:
        if not same_date:
            willGo.append(birthdays[i].person_name)
        elif same_date and temp != '':
            willGo.append(temp)
    temp = ''
    same_date = False
willGo = sorted(willGo)
sys.stdout.write(str(len(willGo)) + '\n')
for b in willGo:
    sys.stdout.write(b + '\n')
