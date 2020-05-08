import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))

evencheck = b % 2

if (evencheck == 0):
    lastnum = int((b/2) + 1)
    a_intermed = b + 1
    a = a_intermed ** (1/f)
    for n in range(1, lastnum):
        intermed1 = n + 1
        F = math.log(intermed1,a)
        print("Ball #", n, "in frame ", F)
        if n == (lastnum - 1):
            point_halfframe = F
    print("-----ease out now----")
    a_intermed = f + 1
    a = a_intermed ** (1/b)
    for n in range(1, lastnum):
        intermed1 = (a ** n)
        intermed2 = intermed1 - 1
        F = intermed2 + point_halfframe
        n = n + (b/2)
        if n > (b/2):
            print("Ball #", n, "in frame ", F)
else:
    lastnum = int((b/2) + 1.5)
    otherlastnum = int((b/2) + 0.5)
    a_intermed = b + 1
    a = a_intermed ** (1/f)
    for n in range(1, lastnum):
        intermed1 = n + 1
        F = math.log(intermed1,a)
        print("Ball #", n, "in frame ", F)
        if n == (lastnum - 1):
            point_halfframe = F
    print("-----ease out now----")
    a_intermed = f + 1
    a = a_intermed ** (1/b)
    for n in range(1, otherlastnum):
        intermed1 = (a ** n)
        intermed2 = intermed1 - 1
        F = intermed2 + point_halfframe
        n = n + (b/2) + 0.5
        if n > (b/2):
            print("Ball #", n, "in frame ", F)
