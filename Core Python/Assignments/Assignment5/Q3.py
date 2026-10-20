'''3. Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full. 
'''
n = int(input("Enter Number of passenger: "))
total_cost = 0

for i in range(1,n+1):
    age = int(input("Enter age: "))
    ticket_cost = int(input('Enter ticket cost: '))
    
    if age < 12:
        discount = ticket_cost * 30 / 100
        total_cost += ticket_cost - discount
         
    elif age > 59:
        discount = ticket_cost * 50 / 100
        total_cost += ticket_cost - discount
    else:
        total_cost += ticket_cost

print('Total Amount:',total_cost)


         