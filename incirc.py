import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))

lastnum = b + 1

for n in range(1, lastnum):
    intermed1 = n - b
    intermed2 = intermed1/(-1)
    intermed3 = intermed2 ** 2
    intermed4 = intermed3 / (b ** 2)
    intermed5 = intermed4 - 1
    intermed6 = intermed5 * (-1)
    intermed7 = intermed6 * (f ** 2)
    F = math.sqrt(intermed7)
    print("Ball #", n, "in frame ", F)
