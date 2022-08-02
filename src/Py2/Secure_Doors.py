# Secure Doors
# Solution by Hasan Kalzi 02-08-2022
# Link to problem in Kattis: https://open.kattis.com/problems/securedoors
from sys import stdin, stdout


class Employees:
    def __init__(self, name):
        self.name = name
        self.in_check = 0
        self.out_check = 0

    def check_activity(self, status):
        if status == "entry":
            self.in_check += 1
            self.out_check = 0
            if self.in_check == 1:
                stdout.write(self.name + " entered\n")
            else:
                stdout.write(self.name + " entered  (ANOMALY)\n")
        else:
            self.out_check += 1
            if self.out_check == 1 and self.in_check > 0:
                stdout.write(self.name + " exited\n")
            else:
                stdout.write(self.name + " exited (ANOMALY)\n")
            self.in_check = 0


n = int(stdin.readline())
names = []
log = []
for _ in range(n):
    s, n = stdin.readline().strip().split()
    if n not in names:
        names.append(n)
        log.append(Employees(n))
    log[names.index(n)].check_activity(s)
