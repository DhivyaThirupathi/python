choice = input("Type 'F' to convert from F to C or Type 'C' to convert from C to F:")
if choice == 'F':
    F=float(input("Enter the temperature in Fahrenheit: "))
    C=((F-32)*(5/9))
    print("Fahrenheit to Celsius",C)
elif choice == 'C':
    c=float(input("Enter the temperature in Celsius: "))
    f=((9/5)*c)+32
    print("Celsius to Fahrenheit",f)
else:
    print("Value is in the wrong format!!")
