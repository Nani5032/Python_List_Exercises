#this program is to interchange first and last elements in the list
my_list = []

n = int(input('enter number of elements in list:'))

for i in range(0, n):
    #print('enter element ', i)
    element = int(input(f'enter element {i}: '))
    my_list.append(element)


print(my_list)

my_list[0], my_list[-1] = my_list[-1], my_list[0]

print('list after interchanging first and last elements', my_list)

# second way of taking input using map function
# by using below method we can enter all the inputs in single line by giving space

my_list2 = list(map(int, input('enter numbers:').strip().split()))

print(my_list2)

size = len(my_list2)

temp = my_list2[0]
my_list2[0] = my_list2[size -1]
my_list2[size -1] = temp


print('list after interchanging first and last elements', my_list2)
