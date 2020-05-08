import math

pi = 22/7

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
B = ((2.0 * pi)/(4.0 * f)) #finding the value of b in the equation
lastnum = b + 1
check = []

for n in range(1, lastnum):
    intermed1 = (n / b)
    intermed2 = intermed1 - 1
    intermed3 = math.asin(intermed2)
    intermed4 = intermed3 + 1.5
    F = (intermed4 / B)
    F_check = round(F)
    check.append(F_check)

checking = 0
for i in range(0, (lastnum-1)):
    for p in range(0, (lastnum-1)):
        if check[i] == check[p] and (i != p):
            checking = checking + 1

if checking > 0:
    print("There are not enough frames. Reduce number of balls or increase number of frames")

for n in range(1, lastnum):
    print("Ball #", n, "in frame ", check[n-1])
