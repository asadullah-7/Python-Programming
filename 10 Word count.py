# line = "Asad is a good boy."
# count = 1
# for i in line:
#     if i == " ":
#         count += 1


# print("Total words in sentence are: ",count)

line = " Asad is   a good boy."
words = line.split()
count = len(words)

print("Total words in the sentence are: ",count)