# Hanging Out on the Terrace
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/hangingout

allowed, number_of_groups = [int(x) for x in input().split()]
currently_on_terrace = 0
not_allowed = 0
for _ in range(number_of_groups):
    enter_or_leave, persons_in_group = input().split()
    if enter_or_leave == "enter":
        if currently_on_terrace + int(persons_in_group) <= allowed:
            currently_on_terrace += int(persons_in_group)
        else:
            not_allowed += 1
    else:
        currently_on_terrace -= int(persons_in_group)
print(not_allowed)
