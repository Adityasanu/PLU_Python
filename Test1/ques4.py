# 4. Print the multiplication table of a given number up to 10.
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)