import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))

lastnum = b + 1

for n in range(1, lastnum):
    intermed1 = n ** 2
    intermed2 = intermed1 / (b ** 2)
    intermed3 = intermed2 - 1
    intermed4 = intermed3 * (-1)
    intermed5 = intermed4 * (f ** 2)
    intermed6 = math.sqrt(intermed5) * (-1)
    F = intermed6 + f
    print("Ball #", n, "in frame ", F)
