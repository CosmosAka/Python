# 2x2 matrix solver

print("Hi!\nThis program will help you to add the two-by-two matrix")

a11 = int(input("Please write the number of the 1st row and 1st column for the 1st matrix:\n"))
a12 = int(input("Please write the number of the 1st row and 2nd column for the 1st matrix:\n"))
a21 = int(input("Please write the number of the 2st row and 1st column for the 1st matrix:\n"))
a22 = int(input("Please write the number of the 2st row and 2nd column for the 1st matrix:\n"))

print("Thanks! Now, write the numbers for the second matrix:\n")

b11 = int(input("Please write the number of the 1st row and 1st column for the 2nd matrix:\n"))
b12 = int(input("Please write the number of the 1st row and 2nd column for the 2nd matrix:\n"))
b21 = int(input("Please write the number of the 2st row and 1st column for the 2nd matrix:\n"))
b22 = int(input("Please write the number of the 2st row and 2nd column for the 2nd matrix:\n"))

print("Thanks! All that remains is to wait!\n")

c11 = a11 + b11
c12 = a12 + b12
c21 = a21 + b21
c22 = a22 + b22


print(f"Thanks for waiting!\nResult:\n[" + str(c11) + "  " + str(c12) + "]\n[" + str(c21) + "  " + str(c22) + "]")
