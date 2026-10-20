#e. x - x2/3 + x3/5 - x4/7 + …. to n terms 
x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))
total = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        total = total + x ** i / (2 * i - 1)
    else:
        total = total - x ** i / (2 * i - 1)

print("Sum =", total)