#1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.
u_id = 'ritesh_pimparwar'
passw = 'ritesh123'

for i in range(1,4):
    user_id = input('Enter user id: ')
    password = input('Enter password: ')
   
    if u_id == user_id and passw == password :
        print('Login Sucessful')
        break
    else:
        print('Invalid Credentilas, Re-enter the credentials.')
        
else:
    print('Login Failed. Maximum attempts reached..!')