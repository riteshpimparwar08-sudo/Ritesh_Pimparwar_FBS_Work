# Write a program to enter P, T, R and calculate compound interest.

P = float(input("Enter principal amount: "))
T = float(input("Enter time: "))
R = float(input("Enter rate: "))

amount = P * (1 + R / 100) ** T
print("Amount is:", amount)

compound_interest = amount - P

print("Compound interest is:", compound_interest)