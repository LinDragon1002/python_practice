datas = []
name = ["Taipei","Taichung","Tainan"]
ans2 = []
ans3 = []
for i in range(15):
    datas.append(float(input()))
print(f"{sum(datas[5:10]) / 5:.3f}")
for i in range(0,15,5):
    temp = round(sum(datas[i:i+5]) / 5,1)
    ans3.append(temp)
    ans2.append(datas[i+5-2])

print(f"{name[ans2.index(max(ans2))]}:{max(ans2):.1f}")
print(name[ans3.index(max(ans3))])