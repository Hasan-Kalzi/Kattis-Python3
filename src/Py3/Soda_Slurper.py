# Soda Slurper
# Solution by Hasan Kalzi 14-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/sodaslurper
import sys

if __name__ == '__main__':
    # after range is the inserted values of e,f,c: int(sys.stdin.readline())
    e, f, c = [int(_) for _ in sys.stdin.readline().split()]
    sodas = int((e + f) / c)
    rest = int((e + f) % c)
    recycled = int(sodas)
    while rest + recycled >= c:
        temp = rest + recycled
        sodas += int(temp / c)
        rest = int(temp % c)
        recycled = int(temp / c)
    sys.stdout.write(str(int(sodas)))
