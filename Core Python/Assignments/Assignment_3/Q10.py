#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
age = int(input('Enter age: '))
gender = input('Enter gender male/female: ')

if gender == 'male':
    if age >= 21:
        print('Eligible for Marriage')
    else:
        print('Not Eligible')
else:
    if age >=18:
        print('Eligible for Marriage')
    else:
        print('Not Eligible')
