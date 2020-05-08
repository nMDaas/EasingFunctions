import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
check = []

evencheck = b % 2
if (evencheck == 0):
    lastnum = int((b/2) + 1)
    a_intermed = b + 1
    a = a_intermed ** (1/f)
    for n in range(1, lastnum):
        intermed1 = n + 1
        F = math.log(intermed1,a)
        F_check = round(F)
        check.append(F_check)
        if n == (lastnum - 1):
            point_halfframe = F
    a_intermed = f + 1
    a = a_intermed ** (1/b)
    for n in range(1, lastnum):
        intermed1 = (a ** n)
        intermed2 = intermed1 - 1
        F = intermed2 + point_halfframe
        F_check = round(F)
        check.append(F_check)
else:
    lastnum = int((b/2) + 1.5)
    otherlastnum = int((b/2) + 0.5)
    a_intermed = b + 1
    a = a_intermed ** (1/f)
    for n in range(1, lastnum):
        intermed1 = n + 1
        F = math.log(intermed1,a)
        F_check = round(F)
        check.append(F_check)
        if n == (lastnum - 1):
            point_halfframe = F
    a_intermed = f + 1
    a = a_intermed ** (1/b)
    for n in range(1, otherlastnum):
        intermed1 = (a ** n)
        intermed2 = intermed1 - 1
        F = intermed2 + point_halfframe
        F_check = round(F)
        check.append(F_check)

checking = 0
for i in range(0, (b-1)):
    for p in range(0, (b-1)):
        if (check[i] == check[p]) and (i != p):
            checking = checking + 1

if checking > 0:
    print("There are not enough frames. Reduce number of balls or increase number of frames")

for n in range(1, (b+1)):
    print("Ball #", n, "in frame ", check[n-1])
