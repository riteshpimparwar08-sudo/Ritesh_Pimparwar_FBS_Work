#11. WAP to check if given number Strong Number. 
n = int(input("Enter a Number : "))
original = n 
total = 0

while n > 0:
    digit = n  % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    total += fact
    n = n // 10
if total == original:
    print('Strong Number')
else:
    print('Not a Strong Number ')

