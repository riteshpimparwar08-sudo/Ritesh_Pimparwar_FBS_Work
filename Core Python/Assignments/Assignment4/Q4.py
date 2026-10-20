#4. WAP to print factorial of a number .
n = int(input("Enter a Number: "))
fact = 1

for i in range(n,0,-1):
    fact *= i
print('Factorial is : ',fact)
