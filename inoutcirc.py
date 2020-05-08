import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))

evencheck = b % 2

if (evencheck == 0):
    lastnum = int((b/2) + 1)
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
        if n == (lastnum - 1):
            point_halfframe = F
    print("-----ease out now----")
    for n in range(1, lastnum):
        intermed1 = n ** 2
        intermed2 = intermed1 / (b ** 2)
        intermed3 = intermed2 - 1
        intermed4 = intermed3 * (-1)
        intermed5 = intermed4 * (f ** 2)
        intermed6 = math.sqrt(intermed5) * (-1)
        F = intermed6 + f + point_halfframe
        n = n + (b/2)
        if n > (b/2):
            print("Ball #", n, "in frame ", F)

else:
    lastnum = int((b/2) + 1.5)
    otherlastnum = int((b/2) + 0.5)
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
        if n == (lastnum - 1):
            point_halfframe = F
    print("-----ease out now----")
    for n in range(1, otherlastnum):
        intermed1 = n ** 2
        intermed2 = intermed1 / (b ** 2)
        intermed3 = intermed2 - 1
        intermed4 = intermed3 * (-1)
        intermed5 = intermed4 * (f ** 2)
        intermed6 = math.sqrt(intermed5) * (-1)
        F = intermed6 + f + point_halfframe
        n = n + ((b/2)+0.5)
        print("Ball #", n, "in frame ", F)
