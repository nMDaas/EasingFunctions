# Easing Functions

## Graphic Presentation
Video at https://youtu.be/a-DvgAZY9c4

![Image of Key](https://github.com/nMDaas/EasingFunctions/blob/master/BallKey.png)

## Application

Easing functions are used in animation for various types of movements. 

These ease in and ease out functions are based on the idea that a ball is moving up and down in a vertical path. The results of the function is also suited for Animate CC which has a keyframe with many frames within which the movement of the ball can be graphically represented. Using the results of these programs, animators can quickly position the balls among the various frames based on the frame number or y coordinate after giving an input of number of balls, number of frames, Factor of elasticity (for elasticity) and the particular easing function. 

## Variables Used

1. f: number of frames
2. b: number of balls 
3. B and a: constants (except for in the elastic function, where B is the y coordinate for the ball)
4. F (in elastic functions): This decides the elasticity of the ball - The higher the value of F, the greater the elasticity

## Note on Ball Numbers and Ball positions

### For all functions (except for the elastic functions):

The frame number is given for a ball number. The ball number is given, assuming its position in the movement of the ball. 

For example, if the number of balls is 10: 
  Ball #1 is @ the 1/10 position of the total distance desired 
  Ball #2 is @ the 2/10 position of the total distance desired 
  Ball #3 is @ the 3/10 position of the total distance desired 
  ... and so on
  
This is a rounded number

### For the elastic functions:

At each frame number, the position of the ball on the y axis is given

This number is not rounded

## Functions 

### 1. Ease in Sine

B =  ((2.0 * pi)/(4.0 * f)) --> B finds the value of b in the formula: a*sin bx + c

y = b[sin(Bx - 1.5)+1] --> Here, b is the number of balls 

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
for n in range(1, lastnum):
    intermed1 = (n / b)
    intermed2 = intermed1 - 1
    intermed3 = math.asin(intermed2)
    intermed4 = intermed3 + 1.5
    F = (intermed4 / B)
    F_check = round(F)
    check.append(F_check)
```

### 2. Ease out Sine 

B =  ((2.0 * pi)/(4.0 * f)) --> B finds the value of b in the formula: a*sin bx + c
y = b sin Bx --> Here, b is the number of balls

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
for n in range(1, lastnum):
    intermed1 = (n/b)
    intermed2 = math.asin(intermed1)
    F = (intermed2/B)
    F_check = round(F)
    check.append(F_check)
```

### 3. Ease in ease out Sine 

B =  ((2.0 * pi)/(4.0 * f)) 
y = [b * {sin (Bx - 1.5) + 1}]/2

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
for n in range(1, lastnum):
    S = 2 * n
    intermed1 = S / b
    intermed2 = intermed1 - 1
    intermed3 = math.asin(intermed2)
    intermed4 = intermed3 + 1.5
    F = intermed4 / B
    F_check = round(F)
    check.append(F_check)
```

### 4. Ease in Quadratic 

a = b/(f*f)
y = (x^2)*a

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
for n in range(1, lastnum):
    intermed1 = n / a
    F = math.sqrt(intermed1)
    F_check = round(F)
    check.append(F_check)
```

### 5. Ease out Quadratic 

a = b/(f*f)
y = [-a * {(-x+f)^2}] + b

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
for n in range(1, lastnum):
    intermed1 = n - b
    intermed2 = intermed1 / (-a)
    intermed3 = math.sqrt(intermed2)
    F = -intermed3 + f
    F_check = round(F)
    check.append(F_check)
```

### 6. Ease in Cubic

a = b/(f^3)
y = a * (x^3)

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
for n in range(1, lastnum):
    intermed1 = n / a
    F = intermed1 ** (1/3)
    F_check = round(F)
    check.append(F_check)
```

### 7. Ease out Cubic 

a = b/(f^3)
y = -a[(-x+f)^3] + b

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
for n in range(1, lastnum):
    intermed1 = n - b
    intermed2 = intermed1/a
    intermed3 = ((-1*intermed2) ** (1/3))*-1
    F = intermed3 + f
    F_check = round(F)
    check.append(F_check)
```

### 8. Ease in Exponential

a = (b+1)^(1/f)
y = [a^(x)] - 1

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
for n in range(1, lastnum):
    intermed1 = n + 1
    F = math.log(intermed1,a)
    F_check = round(F)
    check.append(F_check)
```

### 9. Ease out Exponential 
a = (f+1)^(1/b)
y = log (x+1) to the base a

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
for n in range(1, lastnum):
    intermed1 = (a ** n)
    F = intermed1 - 1
    F_check = round(F)
    check.append(F_check)
```

### 10. Ease in Circular

y = b - square[(b^2) * {(-((x^2)/(f^2) + 1}]

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
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
```

### 11. Ease out Circular 

y = square [-1 * (b^2) * {((-x+f)^2)/(f^2)) -1}

In the program, the y value is input (as the Ball number), giving the frame number, x:

```
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
```

### 12. Ease in Elastic

y = a*sin bx + c

a = (b/2) * [(1/2)^(((-(x-f))/F)-1)] --> b = number of balls
b = (a*(22/7)*((n-f)*-1))/(2*f)
c = b/2 --> b = number of balls

In the program, y is calculated to give the y coordinate of the ball is output.

### 13. Ease out Elastic 

y = a*sin bx + c

a = (b/2) * [(1/2)^((x/F)-1)] --> b = number of balls
b = (a*(22/7)*n)/(2*f)
c = b/2 --> b = number of balls

In the program, y is calculated to give the y coordinate of the ball is output.

### 14. For All Ease in ease out Functions (except for Elastic and Sine)

- If b is an even number (checked by b%2), from frame 1 to b/2, the y coordinates of the ease in function is calculated
- If b is an odd number (checked by b%2), from frame (b/2) + 1 to b, the y coordinates of the ease out function is calculated

### 15. Ease in ease out Elastic 

- If f is an even number (checked by f%2), from frame 1 to b/2, the y coordinates of the ease in function is calculated
- If f is an odd number (checked by f%2), from frame (b/2) + 1 to b, the y coordinates of the ease out function is calculated

## What the checking does (not for the Elastic Functions)

```
 F_check = round(F)
    check.append(F_check)
```

The above code appends a rounded value to the list check[]. 

```
checking = 0
for i in range(0, (lastnum-1)):
    for p in range(0, (lastnum-1)):
        if check[i] == check[p] and (i != p):
            checking = checking + 1

if checking > 0:
    print("There are not enough frames. Reduce number of balls or increase number of frames")

for n in range(1, lastnum):
    print("Ball #", n, "in frame ", check[n-1])
```

The above code checks if, in all the rounded frame numbers, if a frame number is repeated more than once. This would be a problem because two balls cannot be placed in the same frame. Although the code recommeds to change the number of balls or number of frames, for some functions, a repetition in frame number if inevitable. 

## References (Bibliography + Files for Code)

Easing Function References taken from https://easings.net 

### Further Files for each Function 
- Ease in Sine - https://github.com/nMDaas/EasingFunctions/blob/master/easein.py
- Ease out Sine - https://github.com/nMDaas/EasingFunctions/blob/master/easeout.py
- Ease in Ease out Sine - https://github.com/nMDaas/EasingFunctions/blob/master/easeineaseout.py 
- Ease in Quadratic - https://github.com/nMDaas/EasingFunctions/blob/master/inquad.py
- Ease out Quadratic - https://github.com/nMDaas/EasingFunctions/blob/master/outquad.py 
- Ease in Ease out Quadratic - https://github.com/nMDaas/EasingFunctions/blob/master/inoutquad.py
- Ease in Cubic - https://github.com/nMDaas/EasingFunctions/blob/master/incubic.py
- Ease out Cubic - https://github.com/nMDaas/EasingFunctions/blob/master/outcubic.py
- Ease in Ease out Cubic - https://github.com/nMDaas/EasingFunctions/blob/master/inoutcubic.py
- Ease in Exponential - https://github.com/nMDaas/EasingFunctions/blob/master/inexpo.py
- Ease out Exponential - https://github.com/nMDaas/EasingFunctions/blob/master/outexpo.py 
- Ease in Ease out Exponential - https://github.com/nMDaas/EasingFunctions/blob/master/inoutexpo.py
- Ease in Circular - https://github.com/nMDaas/EasingFunctions/blob/master/incirc.py
- Ease out Circular - https://github.com/nMDaas/EasingFunctions/blob/master/outcirc.py
- Ease in Ease out Circular - https://github.com/nMDaas/EasingFunctions/blob/master/inoutcirc.py
- Ease in Elastic - https://github.com/nMDaas/EasingFunctions/blob/master/inelastic.py
- Ease out Elastic - https://github.com/nMDaas/EasingFunctions/blob/master/outelastic.py
- Ease in Ease out Elastic - https://github.com/nMDaas/EasingFunctions/blob/master/inoutelastic.py
