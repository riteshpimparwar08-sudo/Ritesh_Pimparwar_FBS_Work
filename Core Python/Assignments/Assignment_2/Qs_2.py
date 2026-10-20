#2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
#F = (C * 9/5) + 32
 
Temp = float(input("Enter temperature in Celsius: "))

fahrenheit = (Temp * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)