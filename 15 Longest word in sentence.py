line = "Asad is a good boy , he is supercalafragilisticexpialadiocious"
list = line.split()
max = list[0]
for i in list:
    if len(i) > len(max):
        max = i
print("Longest word is: ",max, "and its length is ", len(max), " charachters")
    
# ALSO:
# line = "Asad is a good boy , he is supercalafragilisticexpialadiocious"

# words = line.split()
# longest = max(words, key=len)

# print("Longest word is:", longest)
# print("Length is:", len(longest))
