import math

f = int(input("Number of frames: "))
b = int(input("Number of balls: "))
F = int(input("Factor of elasticity (the higher, the greater): "))
pi = 22/7

lastnum = f + 1

for n in range(1, lastnum):
    a = (b/2)*((1/2) ** ((n/F)-1))
    sinpart = math.sin((a*(22/7)*n)/(2*f))
    asinpart = a * sinpart
    B = asinpart + (b/2)
    print("In frame ", n, " place ball #", B)
