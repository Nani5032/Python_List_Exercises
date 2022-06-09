from typing import Counter

lst = [6,5,4,9,8,5,3,1,6,8,4,6,1,6,3,5,4,9,6,4,6,5,1,6,5,4,1,6]
myset = set(lst) 
#making set so that duplicates will be removed
#looping over set and using count() function to find the count and entering them in dictionaries
mydict = {}
print("given list: ", lst)
print("making set using given list: ", myset)
for i in myset:
    mydict[i] = lst.count(i)
print("making dictionary of elements and count using count() method: ", mydict)

# counter() method can also be used to get a dictionary with keys and elements and values as count of those elements, counter() method returns a dictionary, below is the example of that

dict2 = Counter(lst)
print("dictionary using counter method: ", dict(dict2))


#below is the user defined count function

def mycount(lst, x):
    count1 = 0
    for i in lst:
        if i == x:
            count1 = count1 + 1
    return count1

print("user defined count method: ", mycount(lst, 1))