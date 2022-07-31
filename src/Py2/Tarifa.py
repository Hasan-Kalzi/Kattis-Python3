# Tarifa
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/tarifa
from sys import stdin, stdout
allowed_megabytes = int(stdin.readline())  # The provider will let Pero use up X megabytes to surf the internet per month
amount_months = int(stdin.readline())  # N  months of using the plan
surf_left = allowed_megabytes  # the cumulative surf to the next month.
for _ in range(amount_months):
    surf_left -= int(stdin.readline())  # minus month's usage
    surf_left += allowed_megabytes  # add new month's surf
stdout.write(str(surf_left))
