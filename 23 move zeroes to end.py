myList = [1,2,3,0,32,5,0,6,5,98,0,6,5,4,87,0,3,2,6,54,9,7,0,0,0,3,23,2,44,20,36320,00,0,0,215]

non_zeroes = [i for i in myList if i != 0]
zeroes = [i for i in myList if i == 0]
myList = non_zeroes + zeroes

print(myList)
