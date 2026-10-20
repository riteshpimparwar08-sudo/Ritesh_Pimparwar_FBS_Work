#Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random 
username = 'Ritesh'
passw = 'Ritesh@123'

user_1 = input('Enter username: ')
passw_1 = input('Enter password: ')

captcha = random.randint(1000,9999)

if username == user_1 and passw == passw_1 :
    print('Login Sucessful!')
    print(captcha)
    captcha_1 = int(input('Enter captcha:' ))
    if captcha == captcha_1:
        print('Sucessful')
    else:
        print('failed')
else:
    print('Invalid Credentials!')

 