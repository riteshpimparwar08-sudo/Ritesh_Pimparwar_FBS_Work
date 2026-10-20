# program to find roots of quadratic equation.

# Program to find roots of quadratic equation

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b ** 2 - 4 * a * c

root1 = (-b + D ** 0.5) / (2 * a)
root2 = (-b - D ** 0.5) / (2 * a)

print("The roots of the quadratic equation are:", root1, "and", root2)

