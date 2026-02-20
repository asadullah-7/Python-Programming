myList = [2,5,8,7,4,1,9,6,3,2,5,7,8,4,5,6,1,3,6,5,4,7,8,96,0]
n = len(myList)
for i in range(n):
    for j in range(0, n-i-1):
        if (myList[j]>myList[j+1]):
            myList[j],myList[j+1]=myList[j+1],myList[j]
print(myList)