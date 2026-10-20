#1. Write a program to calculate the percentage of student based on  marks of any 5 subjects.

m1 = int(input("Enter mark of subject 1 : " ))
m2 = int(input("Enter mark of subject 2 : " ))
m3 = int(input("Enter mark of subject 3 : " ))  
m4 = int(input("Enter mark of subject 4 : " ))
m5 = int(input("Enter mark of subject 5 : " ))

total_marks = m1 + m2 + m3 + m4 + m5

percentage = total_marks / 500 *100
print("Total marks is : ", total_marks)
print("Percentage of marks is : ", percentage)