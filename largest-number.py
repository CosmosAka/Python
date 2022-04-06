#Largest and smallest number

print("This program will help you find the largest and the smallest of three different numbers you enter!")
first = float(input("Write the first number:\n"))
second = float(input("Also, write the second number:\n"))
third = float(input("Finally, write the third number:\n"))
list = [first, second, third]
max = max(list)
min = min(list)
print(f"The largest number is {max} and the smallest is {min}")
