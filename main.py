x = int(input("Enter a number: "))
y = x%2
z = False
if y == 0:
    z = True
if not z:
    print(x, "is not an even number.")
else:
    print(x, "is an even number.300")
a = 30
b = 7
if a > 10 or b>10:
    print("One of the values are greater than 10.")
if a>10 and b>10:
    print("Both values are greater than 10.")
else:
    print("One of the values are lesser than 10")