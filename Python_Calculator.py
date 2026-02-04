print('\n"PYTHON CALCULATOR"')

print("\nHere you can find the 'Addition', 'Substraction', 'Multiplication', 'Division', 'Remainder' and 'Square'.\n")
print("First enter the values and then")
print("Type : (+,-,*,/,**,%)\n\n+ : Addition\n- : Substraction\n* : Multiplication\n/ : Division\n** : Square\n% : Remainder\nRespectively...\n")

a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))

print("a is,",a)
print("b is,",b)

operator = input("Enter operation (+, -, *, /, **, %): ")

if operator == '+':
    print("Addition is :" ,a+b)
elif operator == '-':
    print("Substraction is :", a-b)
elif operator == '*':
    print("Multiplication is :", a*b)
elif operator == '/':
    print("Division is :", a/b)
elif operator == '**':
    print("Square of,\na :",a**2)
    print("b :",b**2)
elif operator == '%':
    print("Remainder is :", a%b)
else :
    print("Invalid Operation, Try Again...")

# Code to Find Average of Two Numbers

aveg = input("Do you find the Average of Number?\n(Yes/No) : ")
if aveg.lower() == "yes":
    print(f"The Average of {a} and {b} is ",(a+b)/2)
else :
    print("Thank You...")

# Code to Print the Table of any Number

table = input("Do you want to calculate the Table of any Number?\n(Yes/No) : ")

if table.lower() == "yes":
    t1 = int(input("Enter the Table Number : "))
    print(f"{t1} * 1 =",t1*1)
    print(f"{t1} * 2 =",t1*2)
    print(f"{t1} * 3 =",t1*3)
    print(f"{t1} * 4 =",t1*4)
    print(f"{t1} * 5 =",t1*5)
    print(f"{t1} * 6 =",t1*6)
    print(f"{t1} * 7 =",t1*7)
    print(f"{t1} * 8 =",t1*8)
    print(f"{t1} * 9 =",t1*9)
    print(f"{t1} * 10 =",t1*10)
    print("Thank You for using this Smart Calculator, hope it is helpful :)")
elif table.lower() == "no":
    print("Thank you...")
else:
    print("Give Valid Input (Yes/No)...")
    print("Thank you...")        

