lst = [98,76,54,13,51,98,43,51,68,74,94,32,13,2,3]
# using loops to find sum and avg of lost elements
lst_sum = 0
lst_avg = 0
count = 0
for i in lst:
    lst_sum = lst_sum + i
    count = count + 1
lst_avg = lst_sum / count
print("sum of elements of list: ", lst_sum)
print("avg of elements of list: ", lst_avg)

# below mehtods are by using inbuilt methods
print('using sum() method : ', sum(lst))
print('avg is : ', sum(lst) / len(lst))
