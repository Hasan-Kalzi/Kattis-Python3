# Heart Rate
# Solution by Hasan Kalzi 08-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/heartrate

for _ in range(int(input())):
    b, p = [float(x) for x in input().split()]
    bpm = (60 * b) / p
    print("%.4f" % (bpm - (60 / p)), " ", "%.4f" % bpm, " ", "%.4f" % (bpm + (60 / p)))
