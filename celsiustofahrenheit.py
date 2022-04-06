# Converter from Celsius to Fahrenheit or vice versa

temp = input("Welcome to temperature converter!\nWrite 1 or 2 to choose temperature conversion options:\n1) Celsius °C to Fahrenheit °F\n2) Fahrenheit °F to Celsius °C\n")
temp = int(temp)

if temp == 1:
    print("You chose conversion from Celsius to Fahrenheit")
    cel1 = input("Write the temperature in Celsius °C:\n")
    cel2 = float(cel1)
    con1 = cel2/5*9+32
    cel3 = round(con1, 2)
    print(f"Result: {cel1} °C Celsius equals to " + str(cel3) + " °F Fahrenheit\n\nThank you for using our converter!\nTo use the converter again, restart the program!")
elif temp == 2:
    print("You chose conversion from Fahrenheit to Celsius")
    far1 = input("Write the temperature in Fahrenheit °F:\n")
    far2 = float(far1)
    con2 = (far2-32)*5/9
    far3 = round(con2, 2)
    print(f"Result: {far1} °F Fahrenheit equals to " + str(far3) + " °C Celsius\n\nThank you for using our converter!\nTo use the converter again, restart the program!")
else: print("You did something wrong!\nTry starting over!")
