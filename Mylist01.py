#mylist = [123, 2, 34, 44, 58, 63]
#mylist.append(57)
#mylist.sort()
#print(mylist)

#newlist = mylist.copy()
#newlist.append(1000)
#print(newlist)

#newvalue = int(input("Please enter a number"))
#if newvalue in mylist:
    #print("Element is in the list")
#else:
    #print("Element is not in the list")

oddlist = [1, 3, 5, 7, 9]
evenlist = [2, 4, 6, 8, 10]
for i in range(0, len(oddlist)):
    newlist = int(oddlist[i]) + int(evenlist[i])
    print(newlist)