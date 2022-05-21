'''
split() function is used to split input string into list of strings, by default it takes space as split parameter
example - 
user input -  1 2 3 4 5
after using split - ['1','2','3','4','5']
map() function maps each element with given function(ijn this case its 'int')
'''

a, b = list(map(int, input('enter 2 numbers: ').split()))

print(a, b)

def maximum(a, b):
    if a > b:
        return a
    if b > a:
        return b

print('bigger number is:', maximum(a, b))
