#7. Find the sum of three-digit number.
num = int(input("Enter a three-digit number: "))
sum = 0

d = num % 10
sum += d
num = num // 10
d = num % 10
sum += d
num = num // 10
d = num % 10
sum += d
    
print("Sum of digits:", sum)
 
 