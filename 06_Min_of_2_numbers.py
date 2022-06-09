'''
split() function is used to split input string into list of strings, by default it takes space as split parameter
example - 
user input -  1 2 3 4 5
after using split - ['1','2','3','4','5']
map() function maps each element with given function(in this case its 'int')
'''

a, b = map(int, input('enter 2 numbers: ').split())

print('entered numbers are :', a, b)

def minimum(a, b):
    if a <= b:
        return a
    if b < a:
        return b

print("smaller number is :", minimum(a, b))

#another way using inbuild min() function

print('small num is ', min(a,b))