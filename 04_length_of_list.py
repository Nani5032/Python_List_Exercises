# we will find length of list without using inbuilt function

'''
split() function is used to split input string into list of strings, by default it takes space as split parameter
example - 
user input -  1 2 3 4 5
after using split - ['1','2','3','4','5']
'''

from operator import length_hint


my_list = list(input('enter list elements: ').split())
print(my_list)
count = 0
for i in my_list:
    count += 1
print(count)

# above method is considered slow

print(len(my_list)) # -> second fastest
print(length_hint(my_list)) # -> fastest, this method is from operator class

