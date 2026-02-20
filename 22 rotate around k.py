myList = [1,2,3,4,5,6,7,8,9,10]
k = 2

k = k%len(myList)
rotated = myList[k:]+myList[:k]
print(rotated)
