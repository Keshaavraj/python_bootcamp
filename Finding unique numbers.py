# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
numbers= int(input("Enter total number you want to add:" ))
my_list=[]

for i in range(numbers):
    my_list.append(float(input("Enter the number: ")))

print(my_list)

unique_list=[]

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)
#
# Write your code here.
#
print("The list with unique elements only:",unique_list )
# print(my_list)
