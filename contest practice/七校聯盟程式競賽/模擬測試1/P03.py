st = input()
temp = [ord(i) for i in st]
for i in range(len(temp)-1):
    if temp[i] <= temp[i+1]:
        print(3)
        break
else:
    print(1)
