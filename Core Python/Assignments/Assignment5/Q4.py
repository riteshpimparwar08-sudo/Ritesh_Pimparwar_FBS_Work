#4. WAP to print Armstrong number within a given range
start = int(input('Enter starting nunmber: '))
end = int(input("Enter Ending Number: "))

for n in range(start,end+1):
    original = n 
    temp = n 
    total = 0
    power = len(str(n))

    while temp > 0:
        d = temp % 10
        total += d ** power
        temp = temp // 10 

    if original == total:
        print(original,end=' ')




