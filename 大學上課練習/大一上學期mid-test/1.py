'''
四. 計算租金
    有一家租車公司的「出租費用」以車輛的「排氣量」及「出租天數」為依據，說明如下：

    1. 輸入:
       多組「排氣量」及「出租天數」(存在 list 中的資料)

    2. 處理:
       (1) 如果出租車輛的排氣量大於(含)2200, 每天租金2,500元
       (2) 如果排氣量不足2200且排氣量大於(含)1800, 每天租金2,000元
       (3) 如果排氣量不足1800, 每天租金1,600元

    3. 輸出:
       出租費用 (四捨五入至整數, 加入千分位符號)

    4. 測試資料:
       data = [(2200,2), (2300,3), (1800,3), (1900,2), (1500,4)]

    5. 參考解答:
       租金=5,000元
       租金=7,500元
       租金=6,000元
       租金=4,000元
       租金=6,400元
'''

data = [(2200,2), (2300,3), (1800,3), (1900,2), (1500,4)]

for cc, days in data:
    if cc >= 2200:
        price = 2500
    elif 1800 <= cc < 2200:
        price = 2000
    else:
        price = 1600

    total = price * days
    print(f'租金={total:,.0f}元')