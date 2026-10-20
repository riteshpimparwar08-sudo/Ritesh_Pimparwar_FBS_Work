#2. WAP to print all odd numbers until n. 
n = int(input("Enter a Number :"))

for i in range(1,n):
    if i % 2 != 0:
        print(i)