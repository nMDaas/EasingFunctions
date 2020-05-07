import math

pi = 22/7

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
B = ((2.0 * pi)/(2.0 * f)) #finding the value of b in the equation
lastnum = b + 1

for n in range(0, lastnum):
    S = 2 * n
    intermed1 = S / b
    intermed2 = intermed1 - 1
    intermed3 = math.asin(intermed2)
    intermed4 = intermed3 + 1.5
    F = intermed4 / B
    print("Ball #", n, "in frame ", F)
