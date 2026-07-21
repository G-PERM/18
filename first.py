n1 = float(input("Enter a number: "))
n2 = float(input("Enter another number: "))
o = str(input("Operation: "))
if o == "+":
    print(n1 + n2)
elif o == "-":
    print(n1 - n2)
elif o == "*":
    print(n1 * n2)
elif o == "/":
    print(n1 / n2)
elif o == "//":
    print(int(n1 // n2))
elif o == "%":
    print(n1 % n2)
elif o == "**":
    print(n1 ** n2)
else:
    print("Invalid operation")