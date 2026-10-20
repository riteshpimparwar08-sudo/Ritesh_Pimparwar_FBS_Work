#Write a program to calculate profit or loss.
cost_price = float(input('Enter cost price: ' ))
selling_price =float(input('Enter selling price: '))

if selling_price > cost_price :
    print('profit')
elif cost_price > selling_price:
    print('loss')
else:
    print('No profit No loss')