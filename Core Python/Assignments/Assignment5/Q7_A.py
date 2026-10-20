#a. 1! + 2! + 3! + 4! + …..n!

n = int(input("Enter n: "))
total = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    total = total + fact

print("Sum =", total)