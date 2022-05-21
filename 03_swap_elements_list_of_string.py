# hello world
# heool wlrod
my_list = input('enter list of strings: ').split()
print(my_list)

a, b = input('enter 2 characters to swap: ').split()
print(a, b)

result = [str.replace(a,'p').replace(b,a).replace('p',b) for str in my_list] 
print(result)
