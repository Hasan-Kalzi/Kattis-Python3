# Spavanac
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/spavanac

inserted_time = [int(x) for x in input().split()]  # [Hour,minutes]
# in case the minutes less than 45 the hour scorpion will go back one and calculate the minutes
if inserted_time[1] - 45 < 0:
    inserted_time[0] -= 1  # decrease hour by 1
    inserted_time[1] = 60 + inserted_time[1] - 45
# in case the minutes over or equals 45
else:
    inserted_time[1] = inserted_time[1] - 45

# in case the hour got negative
if inserted_time[0] < 0:
    inserted_time[0] = 23
# print the time before 45 minutes of the inserted time
print(inserted_time[0], inserted_time[1])
