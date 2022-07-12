# ICPC Awards
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/icpcawards

number_of_teams = int(input())
institution = []
teams = []
for _ in range(number_of_teams):
    prize = input().split()
    # if there is no duplicates in the institutions add them to winners list
    if prize[0] not in institution:
        institution.append(prize[0])
        teams.append(prize[1])
    # we want the first 12 winners. We quit the loop when we have them to save time and memory
    if len(institution) == 12:
        break

# The output should contain 12 lines describing 12 winners. In each line,
# you should print the university name and the team name separated by a single space.
# The winners should be listed in the same order as the input.
for i in range(12):
    print(institution[i], teams[i])
