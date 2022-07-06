# Eligibility
# Solution by Hasan Kalzi 24-03-2021
# Link to problem in https://open.kattis.com/problems/eligibility
import sys

for _ in range(int(sys.stdin.readline())):
    name, date1, date2, courses = sys.stdin.readline().split()
    year1 = date1.split('/')[0]
    year2 = date2.split('/')[0]
    if year1 >= '2010' or year2 >= '1991':
        sys.stdout.write(name + " eligible\n")
    elif int(courses) >= 41:
        sys.stdout.write(name + " ineligible\n")
    else:
        sys.stdout.write(name + " coach petitions\n")
