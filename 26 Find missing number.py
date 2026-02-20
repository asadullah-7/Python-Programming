myList = [1,2,4,5]
n = len(myList)+1
formula = n*(n+1)//2
totalSum = sum(myList)

missing = formula-totalSum
print ("missing from array is : ",missing)

