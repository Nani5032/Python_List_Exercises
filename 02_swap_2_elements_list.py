'''
strip() function is used to remove the leadng and trailing characters of the string

'''

my_list = list(map(int, input('enter list elements:').strip().split()))

size = len(my_list)

print(f'enter 2 list indexes between 0 and {size-1}')

a, b = list(map(int, input().strip().split()))

my_list[a], my_list[b] = my_list[b], my_list[a]

print(my_list)