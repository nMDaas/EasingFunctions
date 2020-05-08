import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
a_intermed = b + 1
a = a_intermed ** (1/f)
check = []

lastnum = b + 1
for n in range(1, lastnum):
    intermed1 = n + 1
    F = math.log(intermed1,a)
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
