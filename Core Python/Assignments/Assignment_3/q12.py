#12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter a three digit number:'))

d1 = num % 10
num = num // 10


d2 = num % 10
num = num // 10

d3 = num % 10 
if d1 == d3:
    print('Palindrome')
else:
    print('Not a palindrome')
