#10. WAP to check if given number is Perfect Number. 
n = int(input("Enter a Number: "))
total = 0

for i in range(1,n):
    if n % i ==0:
        print(i)
        total += i
if total == n:
        print('Perfect Number')
else:
    print('Not a perfect Number')