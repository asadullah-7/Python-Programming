myList = [1,2,3,4,5,6,7,8,9,10]
target = 9
n = len(myList)
found = False
for i in range(n):
    for j in range(i+1, n):
        if myList[i]+myList[j] == target:
            print(f"Sum of {i+1} and {j+1} = {target}")
            fount = True
            break
    if found:
        break