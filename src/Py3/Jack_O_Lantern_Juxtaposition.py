# Jack-O'-Lantern Juxtaposition
# Solution by Hasan Kalzi 10-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/jackolanternjuxtaposition
import io
import os
import sys

a, b, c = map(int, io.BytesIO(os.read(0, os.fstat(0).st_size)).readline().decode().split())

sys.stdout.write(str(a * b * c))
