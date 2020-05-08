import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
check = []

lastnum = b + 1

for n in range(1, lastnum):
    intermed1 = n ** 2
    intermed2 = intermed1 / (b ** 2)
    intermed3 = intermed2 - 1
    intermed4 = intermed3 * (-1)
    intermed5 = intermed4 * (f ** 2)
    intermed6 = math.sqrt(intermed5) * (-1)
    F = intermed6 + f
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
