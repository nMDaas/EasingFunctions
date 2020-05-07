import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
a = b/ (f**3)

lastnum = b + 1

for n in range(1, lastnum):
    intermed1 = n / a
    F = intermed1 ** (1/3)
    print("Ball #", n, "in frame ", F)
