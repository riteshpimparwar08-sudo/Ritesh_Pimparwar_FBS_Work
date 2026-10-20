#b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent) 
n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total = total + n ** i

print("Sum =", total)