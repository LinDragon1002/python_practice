def payment(a,b):
    temp = int(a) - int(b)
    temp1 = [50,10,5,1]
    ans = []
    for i in range(len(temp1)):
        ans.append(temp//temp1[i])
        temp = temp - temp1[i]*ans[i]
    for i in range(len(ans)):
        print(ans[i]) 

a = input()
b = input()
payment(a,b)