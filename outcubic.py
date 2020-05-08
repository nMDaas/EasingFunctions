import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
a = b/ (f**3)
check = []

lastnum = b + 1
for n in range(1, lastnum):
    intermed1 = n - b
    intermed2 = intermed1/a
    intermed3 = ((-1*intermed2) ** (1/3))*-1
    F = intermed3 + f
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
