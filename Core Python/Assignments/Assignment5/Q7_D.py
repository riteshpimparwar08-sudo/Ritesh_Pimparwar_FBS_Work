#d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10 

a = int(input("Enter a: "))
total = 0

for i in range(1, 11):
    total = total + (a ** i) / i

print("Sum =", total)