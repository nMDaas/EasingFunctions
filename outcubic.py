import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
a = b/ (f**3)

lastnum = b + 1
for n in range(1, lastnum):
    intermed1 = n - b
    intermed2 = intermed1/a
    intermed3 = ((-1*intermed2) ** (1/3))*-1
    F = intermed3 + f
    print("Ball #", n, "in frame ", F)
