num = int(input('Enter a number: '))
sum = 0
while(num>0):
    d = num % 10
    print('d:',d)
    num = num // 10
    print('num:',num)

sum += d
print('Sum of digits:',sum)