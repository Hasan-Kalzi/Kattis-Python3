# Damaged Equation
# Solution by Hasan Kalzi 15-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/damagedequation
from sys import stdin, stdout

a, b, c, d = map(int, stdin.readline().split())
no_solution = 1
if a * b == c * d:
    stdout.write(str(a) + ' * ' + str(b) + ' = ' + str(c) + ' * ' + str(d) + '\n')
    no_solution = 0
if a * b == c + d:
    stdout.write(str(a) + ' * ' + str(b) + ' = ' + str(c) + ' + ' + str(d) + '\n')
    no_solution = 0
if a * b == c - d:
    stdout.write(str(a) + ' * ' + str(b) + ' = ' + str(c) + ' - ' + str(d) + '\n')
    no_solution = 0
if d != 0:
    if a * b == int(c / d):
        stdout.write(str(a) + ' * ' + str(b) + ' = ' + str(c) + ' / ' + str(d) + '\n')
        no_solution = 0

if a + b == c * d:
    stdout.write(str(a) + ' + ' + str(b) + ' = ' + str(c) + ' * ' + str(d) + '\n')
    no_solution = 0
if a + b == c + d:
    stdout.write(str(a) + ' + ' + str(b) + ' = ' + str(c) + ' + ' + str(d) + '\n')
    no_solution = 0
if a + b == c - d:
    stdout.write(str(a) + ' + ' + str(b) + ' = ' + str(c) + ' - ' + str(d) + '\n')
    no_solution = 0
if d != 0:
    if a + b == int(c / d):
        stdout.write(str(a) + ' + ' + str(b) + ' = ' + str(c) + ' / ' + str(d) + '\n')
        no_solution = 0

if a - b == c * d:
    stdout.write(str(a) + ' - ' + str(b) + ' = ' + str(c) + ' * ' + str(d) + '\n')
    no_solution = 0
if a - b == c + d:
    stdout.write(str(a) + ' - ' + str(b) + ' = ' + str(c) + ' + ' + str(d) + '\n')
    no_solution = 0
if a - b == c - d:
    stdout.write(str(a) + ' - ' + str(b) + ' = ' + str(c) + ' - ' + str(d) + '\n')
    no_solution = 0
if d != 0:
    if a - b == int(c / d):
        stdout.write(str(a) + ' - ' + str(b) + ' = ' + str(c) + ' / ' + str(d) + '\n')
        no_solution = 0
if b != 0:
    if int(a / b) == c * d:
        stdout.write(str(a) + ' / ' + str(b) + ' = ' + str(c) + ' * ' + str(d) + '\n')
        no_solution = 0
    if int(a / b) == c + d:
        stdout.write(str(a) + ' / ' + str(b) + ' = ' + str(c) + ' + ' + str(d) + '\n')
        no_solution = 0
    if int(a / b) == c - d:
        stdout.write(str(a) + ' / ' + str(b) + ' = ' + str(c) + ' - ' + str(d) + '\n')
        no_solution = 0
    if d != 0:
        if int(a / b) == int(c / d):
            stdout.write(str(a) + ' / ' + str(b) + ' = ' + str(c) + ' / ' + str(d) + '\n')
            no_solution = 0
if no_solution == 1:
    stdout.write("problems ahead\n")
