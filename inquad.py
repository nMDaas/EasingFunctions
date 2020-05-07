import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
x_squared = f*f
a = b / x_squared

lastnum = b + 1

for n in range(1, lastnum):
    intermed1 = n / a
    F = math.sqrt(intermed1)
    print("Ball #", n, "in frame ", F)
