def addition(*data):
    sum=0
    for val in data:
        sum+= val
    return sum

res = addition(10,20,30,40)
print('Addition:',res)