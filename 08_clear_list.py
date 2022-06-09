mylist = list(map(int, input('enter list elements: ').split()))

print(mylist)

#emptying list using del keyword

del mylist[:]

mylist.clear()

print(mylist)

# we can also use clear() mehtod to do this -> mylist.clear()
# or you can simply re initialize list with no element -> mylist = []