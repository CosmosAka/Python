# Program for solving quadratic equations

import math
import sys

#Input from user
print("Welcome to quadratic equation solver!\nThe formula for quadratic equations looks like: ax2+bx+c=0")
a = int(input("Using the formula, write the values for a:\n"))
if a == 0:
    print("a couldn't be equal to 0\nTo use the program again, restart the program!")
    sys.exit()
b = int(input(f"{a}x2+bx+c=0\nNow write a value for b:\n"))
c = int(input(f"{a}x2+{b}x+c=0\nIt remains now to write the values only for c:\n"))
print(f"The quadratic equation looks like this: {a}x2+{b}x+{c}=0")

#Discriminant calculation
dis = (b**2)-(4*a*c)
print(f"Discriminant for this quadratic equation is: {dis}")
dissqrt = math.sqrt(abs(dis))

#Result calculationa
if dis < 0:
    print("Because of negative discriminant, this quadratic equation has no solutions!")
elif dis == 0:
    x_1 = abs(b) + dissqrt
    x_2 = 2 * a
    x3 = round(x_1 / x_2)
    print(f"This quadratic equation has one real root and result is x1 = {x3}")
elif dis > 0:
    x_1 = abs(b) + dissqrt
    x_11 = abs(b) - dissqrt
    x_2 = 2 * a
    x1 = round(x_1 / x_2, 3)
    x2 = round(x_11 / x_2, 3)
    print(f"This quadratic equation has two real roots and result is: x1 = {x1} or x2 = {x2}")
else:
    print("Something went wrong, please try again!")
    sys.exit()
