# Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition:
#a. Children below 12 30% discount
#b. Senior citizen (above 59) = 50% discount
#с. Others need to pay full.

ticket = float(input("Enter ticket amount: "))
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))
age5 = int(input("Enter age of person 5: "))

if age1 < 12:
    t1 = ticket * 0.70
elif age1 > 59:
    t1 = ticket * 0.50
else:
    t1 = ticket

print("Age1 Ticket amount to pay:", t1)

if age2 < 12:
    t2 = ticket * 0.70
elif age2 > 59:
    t2 = ticket * 0.50
else:
    t2 = ticket

print("Age2 Ticket amount to pay:", t2)

if age3 < 12:
    t3 = ticket * 0.70
elif age3 > 59:
    t3 = ticket * 0.50
else:
    t3 = ticket

print("Age3 Ticket amount to pay:", t3)

if age4 < 12:
    t4 = ticket * 0.70
elif age4 > 59:
    t4 = ticket * 0.50
else:
    t4 = ticket

print("Age4 Ticket amount to pay:", t4)


if age5 < 12:
    t5 = ticket * 0.70
elif age5 > 59:
    t5 = ticket * 0.50
else:
    t5 = ticket

print("Age5 Ticket amount to pay:", t5)

total_amount = t1 + t2 + t3 + t4 + t5

print('Total amount to ticket for all of them:',total_amount)






'''total_amount = 0

for i in range(5):
    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket amount: "))

    if age < 12:
        # 30% discount
        ticket = ticket * 0.70

    elif age > 59:
        # 50% discount
        ticket = ticket * 0.50

    else:
        # Full ticket amount
        ticket = ticket

    # Add ticket price to total amount
    total_amount = total_amount + ticket

print("Total ticket amount:", total_amount)
    # Add ticket price to total_amount

print("Total ticket amount:", total_amount)'''
