line = "Asad is a good boy."

words = line.split()
count = 0
for i in words:
    for j in i: 
        count += 1

print("Characteres without spaces are: ", count)

# ALSO IT CAN BE SIMPLER AND PROFESSIONAL:

count2 = len(line.replace(" ",""))
print("Characteres without spaces are: ", count)

print(line.lower())
print(line.upper())
