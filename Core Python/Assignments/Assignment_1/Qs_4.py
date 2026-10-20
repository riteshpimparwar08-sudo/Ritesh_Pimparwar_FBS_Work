#4. Write a program to enter P,T,R and calculate simple interest.
principal_amount = float(input("Enter principal amount: "))
time = float(input("Enter time: "))
rate = float(input("Enter rate: "))

simple_interest = principal_amount * time * rate / 100

print("simple interest is:", simple_interest)