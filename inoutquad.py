import math

f = float(input("Number of frames: "))
b = int(input("Number of balls: "))
x_squared = f*f
a = b / x_squared

evencheck = b % 2

print("Ball # 0 in frame 0")

if (evencheck == 0):
    lastnum = int((b/2) + 1)
    for n in range(1, lastnum):
        intermed1 = n / a
        F = math.sqrt(intermed1)
        print("Ball #", n, "in frame ", F)
        if n == (lastnum - 1):
            point_halfframe = F
    print("-----ease out now----")
    for n in range(1, (lastnum)):
        intermed1 = n - b
        intermed2 = intermed1 / (-a)
        intermed3 = math.sqrt(intermed2)
        F = -intermed3 + f + point_halfframe
        n = n + (b/2)
        if n > (b/2):
            print("Ball #", n, "in frame ", F)

else:
    lastnum = int((b/2) + 1.5)
    otherlastnum = int((b/2) + 0.5)
    for n in range(1, lastnum):
        intermed1 = n / a
        F = math.sqrt(intermed1)
        print("Ball #", n, "in frame ", F)
        if n == (lastnum - 1):
            point_halfframe = F
    print("-----ease out now----")
    for n in range(1, otherlastnum):
        intermed1 = n - b
        intermed2 = intermed1 / (-a)
        intermed3 = math.sqrt(intermed2)
        F = -intermed3 + f + point_halfframe
        n = n + ((b/2)+0.5)
        print("Ball #", n, "in frame ", F)
