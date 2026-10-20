#5. WAP to calculate selling price of book based on cost price and discount.
cost_price = float(input("Enter cost price of the book: "))
discount_percentage = float(input("Enter discount percentage: "))

discount = cost_price * discount_percentage / 100

selling_price = cost_price - discount

print("Selling price of the book is:", selling_price)



