import math

f = int(input("Number of frames: "))
b = int(input("Number of balls: "))
F = int(input("Factor of elasticity (the higher, the greater): "))
pi = 22/7

evencheck = f % 2
if (evencheck == 0):
    lastnum = int((f/2) + 1)
    for n in range(1, lastnum):
        a = (b/2)*((1/2) ** (((-(n-f))/F)-1))
        sinpart = math.sin((a*(22/7)*((n-f)*-1))/(2*f))
        asinpart = a * sinpart
        B = asinpart + (b/2)
        print("In frame ", n, " place ball at y=", B)
        if n == (lastnum - 1):
            point_halfframe = B
    print("-----ease out now----")
    for n in range(1, lastnum):
        a = (b/2)*((1/2) ** ((n/F)-1))
        sinpart = math.sin((a*(22/7)*n)/(2*f))
        asinpart = a * sinpart
        B = asinpart + (b/2) + point_halfframe
        n = n + (f/2)
        print("In frame ", n, " place ball at y=", B)
else:
    lastnum = int((f/2) + 1.5)
    otherlastnum = int((f/2) + 0.5)
    for n in range(1, lastnum):
        a = (b/2)*((1/2) ** (((-(n-f))/F)-1))
        sinpart = math.sin((a*(22/7)*((n-f)*-1))/(2*f))
        asinpart = a * sinpart
        B = asinpart + (b/2)
        print("In frame ", n, " place ball at y=", B)
        if n == (lastnum - 1):
            point_halfframe = B
    print("-----ease out now----")
    for n in range(1, otherlastnum):
        a = (b/2)*((1/2) ** ((n/F)-1))
        sinpart = math.sin((a*(22/7)*n)/(2*f))
        asinpart = a * sinpart
        B = asinpart + (b/2) + point_halfframe
        n = n + (f/2) + 0.5
        print("In frame ", n, " place ball at y=", B)
