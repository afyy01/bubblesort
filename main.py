mylist = [3,1,2,5,4]

mylist.sort(reverse=True)
print(mylist)

#bubble sort

mylist = [3,5,1,2,0]
for i in range (0,len(mylist)):
    for j in range(i, len(mylist)):
        if mylist[i] < mylist[j]:
            mylist[i],mylist[j] = mylist[j], mylist[i]
print("Sorted list is", mylist)