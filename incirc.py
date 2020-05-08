import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
check = []

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
