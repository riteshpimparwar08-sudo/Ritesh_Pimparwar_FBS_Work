#10. Write a program to reverse three-digit number.

num = int(input("Enter three digit number: "))

d1 = num % 10
num = num // 10
d2 = num % 10
num = num // 10
d3 = num % 10

print(d1,d2,d3,sep="")
