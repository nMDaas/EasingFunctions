import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
x_squared = f*f
a = b / x_squared

lastnum = b + 2

for n in range(1, lastnum):
    intermed1 = n - b
    intermed2 = intermed1 / (-a)
    intermed3 = math.sqrt(intermed2)
    F = -intermed3 + f
    print("Ball #", n, "in frame ", F)
