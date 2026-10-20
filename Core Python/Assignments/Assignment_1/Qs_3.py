#3. program to find quotient and remainder of two numbers.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

quotient = num1 // num2
remainder = num1 % num2

print(f'The quotient of {num1} and {num2} is: {quotient}')
print(f'The remainder of {num1} and {num2} is: {remainder}')
