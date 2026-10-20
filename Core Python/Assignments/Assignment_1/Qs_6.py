# write a program to input two angles from user and find the third angle of triangle.
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = 180 - (angle1 + angle2)

print("The third angle of triangle is:", angle3)