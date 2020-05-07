import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
a_intermed = f + 1
a = a_intermed ** (1/b)

lastnum = b + 1
for n in range(1, lastnum):
    intermed1 = (a ** n)
    F = intermed1 - 1
    print("Ball #", n, "in frame ", F)
