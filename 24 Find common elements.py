myList = [1,2,2,3,3,4,4,4,4,4,5,5,2,1,3,5,67,78,3,5,6,4,3]
count = 0
for i in range(len(myList)-1):
    if myList[i] == myList[i+1]:
       print(myList[i], "is repeated consecutively")