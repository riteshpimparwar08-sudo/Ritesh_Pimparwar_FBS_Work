#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = float(input('Enter side 1: '))
b = float(input('Enter side 2: '))
c = float(input('Enter side 3: '))

if a == b == c:
    print('Triangle is Equilateral Triangle')
elif a==b or b==c or c==a:
    print('Triangle is Isosceles Triangle')
else:
    print('Triangle is Scalene Triangle')