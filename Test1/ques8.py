try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    print("Result =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")