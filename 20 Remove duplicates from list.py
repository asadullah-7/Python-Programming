myList = [1,2,3,4,5,6,7,8,9,0,2,2,3,4,5,56,7685646,4256456,45,4,45,45,4,54,5,45,45,3]
unique = []

for num in myList:
    if num not in unique:
        unique.append(num)

print(unique)