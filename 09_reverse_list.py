mylist = [1,2,3,4,5]
mylist = mylist[::-1]
print(mylist)


lst2 = [6,7,8,9,10]
lst2 = list(reversed(lst2))
# reversed returns a list_reversediterator object, thats why we will use list method to convert it to list
print(lst2)


lst3 = [11,12,13,14,15]
lst3.reverse()
# this is an inplace method, the orginal list will be changed
print(lst3)

lst4 = [16,17,18,19,20]
lst5 = []
for i in lst4:
    lst5.insert(0,i)
print(lst5)
# here we are inserting each element at index 0, so automatically first element will be inserted at 0 postion and then second element will be inserted at 0th position, so when each element is inserted at 0th position other elements will be pushed inside.