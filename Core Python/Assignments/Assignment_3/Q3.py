# Write a program to input angles of a triangle and check whether triangle is valid or not.
angle1 = float(input('Enter angle1 of Triangle: '))
angle2 = float(input('Enter angle2 of Triangle: '))
angle3 = float(input('Enter angle3 of Triangle: '))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180:
    print('Triangle is a Valid')
else:
    print('Triangle is not valid')