import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
a = b/ (f**3)

evencheck = b % 2

if (evencheck == 0):
    lastnum = int((b/2) + 1)
    for n in range(1, lastnum):
        intermed1 = n / a
        F = intermed1 ** (1/3)
        print("Ball #", n, "in frame ", F)
        if n == (lastnum - 1):
            point_halfframe = F
    print("-----ease out now----")
    for n in range(1, lastnum):
        intermed1 = n - b
        intermed2 = intermed1/a
        intermed3 = ((-1*intermed2) ** (1/3))*-1
        intermed4 = intermed3 + f
        F = intermed4 + point_halfframe
        n = n + (b/2)
        if n > (b/2):
            print("Ball #", n, "in frame ", F)
else:
    lastnum = int((b/2) + 1.5)
    otherlastnum = int((b/2) + 0.5)
    for n in range(1, lastnum):
        intermed1 = n / a
        F = intermed1 ** (1/3)
        print("Ball #", n, "in frame ", F)
        if n == (lastnum - 1):
            point_halfframe = F
    print("-----ease out now----")
    for n in range(1, otherlastnum):
        intermed1 = n - b
        intermed2 = intermed1/a
        intermed3 = ((-1*intermed2) ** (1/3))*-1
        intermed4 = intermed3 + f
        F = intermed4 + point_halfframe
        n = n + ((b/2)+0.5)
        print("Ball #", n, "in frame ", F)
