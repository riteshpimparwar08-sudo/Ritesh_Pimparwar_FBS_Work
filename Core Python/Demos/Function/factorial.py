def fact(num):
    mult = 1
    for i in range(1, num+1):
        mult  *= i
    return mult

n = 5
res = fact(n)
print('Factorial:',res)