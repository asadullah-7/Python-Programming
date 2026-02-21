line = "Hello my name is Asad Ullah"

freq = {}

for i in line:
    freq[i] = freq.get(i,0)+1

for key,value in freq.items():
    print(key, " occures ",value," times.")