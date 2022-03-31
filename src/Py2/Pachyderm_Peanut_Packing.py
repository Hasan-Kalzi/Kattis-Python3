# Pachyderm Peanut Packing
# Solution by Hasan Kalzi 31-03-2021
# Link to problem i Kattis: https://open.kattis.com/problems/pachydermpeanutpacking
from sys import stdin, stdout


class Box:
    def __init__(self, box):
        self.x1 = float(box[0])
        self.y1 = float(box[1])
        self.x2 = float(box[2])
        self.y2 = float(box[3])
        self.box_type = box[4].strip()

    def box_to_string(self):
        print(self.x1, self.y1, self.x2, self.y2, self.box_type)


class Peanut:
    def __init__(self, peanut):
        self.x = float(peanut[0])
        self.y = float(peanut[1])
        self.peanut_size = peanut[2].strip()

    def peanut_to_string(self):
        print(self.x, self.y, self.peanut_size)


while True:
    boxes = []
    n = int(stdin.readline())
    if n == 0:
        break
    for _ in range(n):
        boxes.append(Box(stdin.readline().split()))
    m = int(stdin.readline())
    for _ in range(m):
        new_peanut = Peanut(stdin.readline().split())
        stdout.write(new_peanut.peanut_size)
        match = 0
        for a_box in boxes:
            if a_box.x1 <= new_peanut.x <= a_box.x2 and a_box.y1 <= new_peanut.y <= a_box.y2:
                if a_box.box_type == new_peanut.peanut_size:
                    stdout.write(" correct\n")
                    match += 1
                    break
                else:
                    stdout.write(" " + a_box.box_type + " \n")
                    match += 1
                    break
        if match == 0:
            stdout.write(" floor\n")
    stdout.write('\n')
