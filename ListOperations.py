# MINIMUM / MAXIMUM VALUE FIND MANNUALY
myList = [43,43,534,34,2,323,-1,43]

minVal = myList[0]
maxVal = myList[0]

for i in myList:
    if i < minVal:
        minVal = i
    if i > maxVal:
        maxVal = i    

print("Minimum Value is: ",minVal)        
print("Maximum Value is: ", maxVal)


# Reverse a List 

print("Reverse of array :", myList[::-1])


