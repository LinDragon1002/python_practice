# 輸入
c,d,n,method = map(int,input("成本,殘值,耐用年限,樹入折舊方法 1直線法 2定律遞減法 3年數合計法 4倍數遞減法 eg:兩個方法輸入12 : ").split(','))

# 儲存使用的方法和年份答案
now_methods = []
ans = []

# 判斷使用幾種方法
for i in range(len(str(method))):
    # 直線法
    if str(method)[i] == '1':
        now_methods.append("直線法")
        for amount in range(1, n + 1):
            tot = int(round((c - d)/n,2))
            ans.append(tot)
    # 定律法
    elif str(method)[i] == '2':
        now_methods.append("定律法")
        for amount in range(0,n):
            R= 1 - ((d / c) ** (1 / n))
            tot = int(round((c*(1-R)**amount)*R,2))
            ans.append(tot)
    # 年數法
    elif str(method)[i] == '3':
        now_methods.append("年數法")
        total = sum(range(1, n + 1))
        for amount in range(0,n):
            tot = int(round((c-d)*(n-amount)/total,2))
            ans.append(tot)
    # 倍數法
    elif str(method)[i] == '4':
        now_methods.append("倍數法")
        for amount in range(0,n):
            R= (2/n)
            tot = int(round((c*(1-R)**amount)*R,2))
            ans.append(tot)

# 輸出表頭
print(f"{'方法順序':<3}",end="")
for i in now_methods:
    print(f"{i:>6}",end="")
print()

# 輸出報表內容
for j in range(n):
    print(f"第{j+1}年",end="")
    for i in range(0,len(ans),n):
        print(f'{ans[i+j]:>10}',end="")
    print()
