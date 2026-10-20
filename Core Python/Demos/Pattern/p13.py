for i in range(1,5):
    for j in range(1,i+1):
        if(j==1 or i==4 or i==j==2 or i==j==3):#i==j
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
