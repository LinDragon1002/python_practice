def encoder(a):
    temp = {"A":"000","B":"001","D":"010","F":"011","K":"100","M":"101","U":"110"}
    ans = ""
    for i in range(len(a)):
        if a[i] in temp:
            ans += temp[a[i]]
        else:
            ans += "***"
    return ans

a = input()
print(encoder(a))
