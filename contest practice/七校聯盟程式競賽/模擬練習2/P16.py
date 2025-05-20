st = input()
temp = []
for i in st:
    temp.append(ord(i))
    
for i in range(len(temp)-1):
    if temp[i] < temp[i+1]:
        