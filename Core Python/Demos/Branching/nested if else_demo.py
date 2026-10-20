gender = input('Enter gender(m/f): ')
age = int(input('Enter age: '))

if (gender == 'f'):
    if(age >= 18):
        print('Eligible for marriage')
    else:
        print('Not Eligible for marriage')
else:
    if(age >= 21):
        print('Eligible for marriage')
    else:
        print('Not Eligible for marriage')