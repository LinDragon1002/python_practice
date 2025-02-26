def decoder(a):
    temp = {"000":"A","001":"B","010":"J","011":"L","100":"M","101":"P","110":"Q","111":"W"}
    ans = ""
    for i in range(0,len(a),3):  
        if a[i:i+3] in temp:
            ans += temp[a[i:i+3]]
        else:
            ans += ""
    return ans

a = input()
print(decoder(a))