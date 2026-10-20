#12. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

n = int(input("Enter a number: "))
original = n
sum = 0 
power = len(str(n)) 

while n > 0:
    d = n % 10
    sum += d **  power 
    n = n // 10

if sum == original:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number')

