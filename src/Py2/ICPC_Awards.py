# ICPC Awards
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/icpcawards
from sys import stdin, stdout

number_of_teams = int(stdin.readline())
institution = []
teams = []
for _ in range(number_of_teams):
    university, team = stdin.readline().strip().split()
    # if there is no duplicates in the institutions add them to winners list
    if university not in institution:
        institution.append(university)
        teams.append(team)
    # we want the first 12 winners. We quit the loop when we have them to save time and memory
    if len(institution) == 12:
        break

# The output should contain 12 lines describing 12 winners. In each line,
# you should print the university name and the team name separated by a single space.
# The winners should be listed in the same order as the input.
for i in range(12):
    stdout.write(str(institution[i]) + ' ' + str(teams[i])+'\n')
