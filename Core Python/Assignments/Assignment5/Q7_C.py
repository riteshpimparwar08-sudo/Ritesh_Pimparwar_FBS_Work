#c. Find the sum of a geometric series from 1 to n where the common ratio is 2. 
n = int(input("Enter number of terms: "))
total = 0

for i in range(n):
    total = total + 2 ** i

print("Sum =", total)