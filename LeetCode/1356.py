arr = [1024,512,256,128,64,32,16,8,4,2,1]
temp = []

for i in range(len(arr)):
    count_ones = format(arr[i], 'b').count('1')
    temp.append((arr[i],count_ones))
temp = sorted(temp, key=lambda x:(x[-1],x[0]))
result = [int(x[0]) for x in temp]
print(result)