# 
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = breadth / 2
pi = 3.14

perimeter_1 = 2 * (length + breadth) - breadth
perimeter_2 = pi * radius 

total_perimeter = perimeter_1 + perimeter_2

area_1  = length * breadth
area_2 = (pi * radius**2) / 2

total_area = area_1 + area_2

print("Total perimeter:", total_perimeter)
print("Total area: ", total_area)


