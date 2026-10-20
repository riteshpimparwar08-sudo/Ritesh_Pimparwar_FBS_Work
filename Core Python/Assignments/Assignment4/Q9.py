#9. WAP to print all numbers in a range divisible by a given number.
n = int(input("Enter a Number: "))

for i in range(1,101):
    if i % n == 0:
        print(i,end=' ')
