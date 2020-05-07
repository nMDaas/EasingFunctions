import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
a_intermed = b + 1
a = a_intermed ** (1/f)

lastnum = b + 1
for n in range(1, lastnum):
    intermed1 = n + 1
    F = math.log(intermed1,a)
    print("Ball #", n, "in frame ", F)
