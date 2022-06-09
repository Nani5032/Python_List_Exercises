mylist = list(map(int, input('enter list elements: ').split()))

print(mylist)

check_element = int(input('enter element you want to check in list: '))

print(check_element)

for i in mylist:
    if i == check_element:
        print('element found')
        break
else:
    print('element not found')

# another way using "in" keyword, return true if present, else false
print(check_element in mylist)

if check_element in mylist:
    print('found')