myList = [1,2,2,3,3,4,4,4,4,4,5,5,2,1,3,5,67,78,3,5,6,4,3]

freq = {}

for i in myList:
    freq[i] = freq.get(i,0)+1

for key,value in freq.items():
    print(key, " occures ",value," times.")