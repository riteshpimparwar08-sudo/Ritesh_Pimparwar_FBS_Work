#8. Write a program to swap two numbers using third variable.
a = int(input("Enter a: "))
b = int(input("Enter b: "))

temp = b
b = a
a = temp

print("After swapping:")
print("a:", a)
print("b:", b)