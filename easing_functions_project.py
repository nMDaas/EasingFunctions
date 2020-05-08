import math

#------------------------------------------------------------------------

print("1. Ease in Sine")
print("2. Ease out Sine")
print("3. Ease in Ease out Sine")
print("4. Ease in Quadratic")
print("5. Ease out Quadratic")
print("6. Ease in Ease out Quadratic")
print("7. Ease in Cubic")
print("8. Ease out Cubic")
print("9. Ease in Ease out Cubic")
print("10. Ease in Exponential")
print("11. Ease out Exponential")
print("12. Ease in Ease out Exponential")
print("13. Ease in Circular")
print("14. Ease out Circular")
print("15. Ease in Ease out Circular")
print("16. Ease in Elastic")
print("17. Ease out Elastic")
print("18. Ease in Ease out Elastic")
#------------------------------------------------------------------------

validcheck = 0

while validcheck == 0:
    function = input("Choose a function: ")

    if (function == "Ease in Sine"):
        functionID = 1
        validcheck = 1
    elif (function == "Ease out Sine"):
        functionID = 2
        validcheck = 1
    elif (function == "Ease in Ease out Sine"):
        functionID = 3
        validcheck = 1
    elif (function == "Ease in Quadratic"):
        functionID = 4
        validcheck = 1
    elif (function == "Ease out Quadratic"):
        functionID = 5
        validcheck = 1
    elif (function == "Ease in Ease out Quadratic"):
        functionID = 6
        validcheck = 1
    elif (function == "Ease in Cubic"):
        functionID = 7
        validcheck = 1
    elif (function == "Ease out Cubic"):
        functionID = 8
        validcheck = 1
    elif (function == "Ease in Ease out Cubic"):
        functionID = 9
        validcheck = 1
    elif (function == "Ease in Exponential"):
        functionID = 10
        validcheck = 1
    elif (function == "Ease out Exponential"):
        functionID = 11
        validcheck = 1
    elif (function == "Ease in Ease out Exponential"):
        functionID = 12
        validcheck = 1
    elif (function == "Ease in Circular"):
        functionID = 13
        validcheck = 1
    elif (function == "Ease out Circular"):
        functionID = 14
        validcheck = 1
    elif (function == "Ease in Ease out Circular"):
        functionID = 15
        validcheck = 1
    elif (function == "Ease in Elastic"):
        functionID = 16
        validcheck = 1
    elif (function == "Ease out Elastic"):
        functionID = 17
        validcheck = 1
    elif (function == "Ease in Ease out Elastic"):
        functionID = 18
        validcheck = 1
    else:
        print("Please choose a valid function.")
#------------------------------------------------------------------------

f = int(input("Number of frames: "))
b = int(input("Number of balls: "))
pi = 22/7
check = []

if ((functionID == 16) or (functionID == 17) or (functionID == 18)):
    F = int(input("Factor of elasticity (the higher, the greater): "))

if ((functionID == 1) or (functionID == 2) or (functionID == 3)):
    B = ((2.0 * pi)/(4.0 * f)) #finding the value of b in the equation
    lastnum = b + 1

if ((functionID == 4) or (functionID == 5) or (functionID == 6)):
    x_squared = f*f
    a = b / x_squared

if ((functionID == 6) or (functionID == 9) or (functionID == 12) or (functionID == 15) or (functionID == 18)):
    evencheck = b % 2

if ((functionID == 7) or (functionID == 8) or (functionID == 9)):
    a = b/ (f**3)
#------------------------------------------------------------------------

if (functionID == 1):
    for n in range(1, lastnum):
        intermed1 = (n / b)
        intermed2 = intermed1 - 1
        intermed3 = math.asin(intermed2)
        intermed4 = intermed3 + 1.5
        F = (intermed4 / B)
        F_check = round(F)
        check.append(F_check)

if (functionID == 2):
    for n in range(1, lastnum):
        intermed1 = (n/b)
        intermed2 = math.asin(intermed1)
        F = (intermed2/B)
        F_check = round(F)
        check.append(F_check)

if (functionID == 3):
    for n in range(1, lastnum):
        S = 2 * n
        intermed1 = S / b
        intermed2 = intermed1 - 1
        intermed3 = math.asin(intermed2)
        intermed4 = intermed3 + 1.5
        F = intermed4 / B
        F_check = round(F)
        check.append(F_check)

if (functionID == 4):
    lastnum = b + 1
    for n in range(1, lastnum):
        intermed1 = n / a
        F = math.sqrt(intermed1)
        F_check = round(F)
        check.append(F_check)

if (functionID == 5):
    lastnum = b + 2
    intermed1 = n - b
    intermed2 = intermed1 / (-a)
    intermed3 = math.sqrt(intermed2)
    F = -intermed3 + f
    F_check = round(F)
    check.append(F_check)

if (functionID == 6):
    if (evencheck == 0):
        lastnum = int((b/2) + 1)
        for n in range(1, lastnum):
            intermed1 = n / a
            F = math.sqrt(intermed1)
            F_check = round(F)
            check.append(F_check)
            if n == (lastnum - 1):
                point_halfframe = F
        for n in range(1, (lastnum)):
            intermed1 = n - b
            intermed2 = intermed1 / (-a)
            intermed3 = math.sqrt(intermed2)
            F = -intermed3 + f + point_halfframe
            F_check = round(F)
            check.append(F_check)
    else:
        lastnum = int((b/2) + 1.5)
        otherlastnum = int((b/2) + 0.5)
        for n in range(1, lastnum):
            intermed1 = n / a
            F = math.sqrt(intermed1)
            F_check = round(F)
            check.append(F_check)
            if n == (lastnum - 1):
                point_halfframe = F
        for n in range(1, otherlastnum):
            intermed1 = n - b
            intermed2 = intermed1 / (-a)
            intermed3 = math.sqrt(intermed2)
            F = -intermed3 + f + point_halfframe
            F_check = round(F)
            check.append(F_check)

if (functionID == 7):
    lastnum = b + 1
    for n in range(1, lastnum):
        intermed1 = n / a
        F = intermed1 ** (1/3)
        F_check = round(F)
        check.append(F_check)

if (functionID == 8):
    lastnum = b + 1
    for n in range(1, lastnum):
        intermed1 = n - b
        intermed2 = intermed1/a
        intermed3 = ((-1*intermed2) ** (1/3))*-1
        F = intermed3 + f
        F_check = round(F)
        check.append(F_check)

if (functionID == 9):
    if (evencheck == 0):
        lastnum = int((b/2) + 1)
        for n in range(1, lastnum):
            intermed1 = n / a
            F = intermed1 ** (1/3)
            F_check = round(F)
            check.append(F_check)
            if n == (lastnum - 1):
                point_halfframe = F
        for n in range(1, lastnum):
            intermed1 = n - b
            intermed2 = intermed1/a
            intermed3 = ((-1*intermed2) ** (1/3))*-1
            intermed4 = intermed3 + f
            F = intermed4 + point_halfframe
            F_check = round(F)
            check.append(F_check)
    else:
        lastnum = int((b/2) + 1.5)
        otherlastnum = int((b/2) + 0.5)
        for n in range(1, lastnum):
            intermed1 = n / a
            F = intermed1 ** (1/3)
            F_check = round(F)
            check.append(F_check)
            if n == (lastnum - 1):
                point_halfframe = F
        for n in range(1, otherlastnum):
            intermed1 = n - b
            intermed2 = intermed1/a
            intermed3 = ((-1*intermed2) ** (1/3))*-1
            intermed4 = intermed3 + f
            F = intermed4 + point_halfframe
            F_check = round(F)
            check.append(F_check)

if (functionID == 10):
    a_intermed = b + 1
    a = a_intermed ** (1/f)
    lastnum = b + 1
    for n in range(1, lastnum):
        intermed1 = n + 1
        F = math.log(intermed1,a)
        F_check = round(F)
        check.append(F_check)

if (functionID == 11):
    a_intermed = f + 1
    a = a_intermed ** (1/b)
    lastnum = b + 1
    for n in range(1, lastnum):
        intermed1 = (a ** n)
        F = intermed1 - 1
        F_check = round(F)
        check.append(F_check)

if (functionID == 12):
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

if (functionID == 13):
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

if (functionID == 14):
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

if (functionID == 15):
    if (evencheck == 0):
        lastnum = int((b/2) + 1)
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
            if n == (lastnum - 1):
                point_halfframe = F
        for n in range(1, lastnum):
            intermed1 = n ** 2
            intermed2 = intermed1 / (b ** 2)
            intermed3 = intermed2 - 1
            intermed4 = intermed3 * (-1)
            intermed5 = intermed4 * (f ** 2)
            intermed6 = math.sqrt(intermed5) * (-1)
            F = intermed6 + f + point_halfframe
            F_check = round(F)
            check.append(F_check)
    else:
        lastnum = int((b/2) + 1.5)
        otherlastnum = int((b/2) + 0.5)
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
            if n == (lastnum - 1):
                point_halfframe = F
        for n in range(1, otherlastnum):
            intermed1 = n ** 2
            intermed2 = intermed1 / (b ** 2)
            intermed3 = intermed2 - 1
            intermed4 = intermed3 * (-1)
            intermed5 = intermed4 * (f ** 2)
            intermed6 = math.sqrt(intermed5) * (-1)
            F = intermed6 + f + point_halfframe
            F_check = round(F)
            check.append(F_check)

if (functionID == 16):
    lastnum = f + 1
    for n in range(1, lastnum):
        a = (b/2)*((1/2) ** (((-(n-f))/F)-1))
        sinpart = math.sin((a*(22/7)*((n-f)*-1))/(2*f))
        asinpart = a * sinpart
        B = asinpart + (b/2)
        print("In frame ", n, " place ball at y=", B)

if (functionID == 17):
    lastnum = f + 1
    for n in range(1, lastnum):
        a = (b/2)*((1/2) ** ((n/F)-1))
        sinpart = math.sin((a*(22/7)*n)/(2*f))
        asinpart = a * sinpart
        B = asinpart + (b/2)
        print("In frame ", n, " place ball at y=", B)

if (functionID == 18):
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



#------------------------------------------------------------------------
inoutcheck = 0
elasticfunctions = [16, 17, 18]
inout = [6, 9, 12, 15]
for e in range(0, 3):
    if (functionID == elasticfunctions[e]):
        inoutcheck = -1
for c in range(0, 5):
    if (functionID == inout[c]):
        inoutcheck = 1
#------------------------------------------------------------------------
checking = 0
if (inoutcheck != 1):
    for i in range(0, (lastnum-1)):
        for p in range(0, (lastnum-1)):
            if check[i] == check[p] and (i != p):
                checking = checking + 1
#------------------------------------------------------------------------
checking = 0
if (inoutcheck == 1):
    for i in range(0, (lastnum-1)):
        for p in range(0, (lastnum-1)):
            if check[i] == check[p] and (i != p):
                checking = checking + 1
#------------------------------------------------------------------------
if checking > 0:
    print("There are not enough frames. Try changing the number of balls or number of frames")

for n in range(1, lastnum):
    print("Ball #", n, "in frame ", check[n-1])
