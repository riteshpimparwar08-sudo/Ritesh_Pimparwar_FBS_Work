#Write a program to check if user has entered correct userid and password.

username = 'Ritesh'
passw = 'Ritesh@123'

user_1 = input('Enter username: ')
passw_1 = input('Enter password: ')

if username == user_1 and passw == passw_1 :
    print('Login Sucessful!')
else:
    print('Invalid Credentials!')