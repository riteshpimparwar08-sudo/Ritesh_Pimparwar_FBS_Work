#2.Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students. 

n = int(input("Enter Number of student: "))

total_percentage = 0.0

for i in range(1,n+1):
    print('Student',i)
    m1 = int(input('Enter mark of subject1: '))
    m2 = int(input('Enter mark of subject2: '))
    m3 = int(input('Enter mark of subject3: '))
    m4 = int(input('Enter mark of subject4: '))
    m5 = int(input('Enter mark of subject5: '))

    total_marks = m1 + m2 + m3 + m4 + m5
    percentage = total_marks  / 500 * 100
    print('percentage is  :',percentage,'%')
    total_percentage += percentage

average = total_percentage / n
print('Average Percentage is:',average,'%')

