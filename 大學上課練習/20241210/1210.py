import math
with open ('cake.csv','r') as infile, open ('out.csv','w',encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [i.strip() for i in data]

    temp = []

    '''
    min_buys = math.inf
    max_buys = -math.inf
    #50項商品的價格
    price=[65, 60, 55, 75, 45, 50, 55, 60, 60, 75, 55, 45, 80, 85, 70, 75, 80, 90, 100, 105, 60, 75, 80, 90, 95, 65, 70, 75, 70, 60, 65, 60, 65, 70, 75, 80, 85, 90, 95, 55, 60, 65, 70, 75, 80, 55, 55, 60, 60, 65]


    for i in data:
        no, *quantity = i.split(',')

        quantity = [int(d) for d in quantity]
        # total = 0
        # for s in range(len(price)):
        #     total += price[s] * quantity[s]
        total = [price[s] * quantity[s] for s in range(len(price))]



        # if max_buys < sum(quantity):
        #     max_buys = sum(quantity)
        # elif min_buys > sum(quantity):
        #     min_buys = sum(quantity)

        max_buys = max(max_buys,sum(quantity))
        min_buys = min(min_buys,sum(quantity))

        temp.append(f'{no:>5}: 購買{sum(quantity):>3}個{sum(total):>6}元\n')

    temp[-1] = temp[-1].strip()
    outfile.writelines(temp)
    print(f'最少 {min_buys}')
    print(f'最多 {max_buys}')
    '''
    items = [0] * 50
    cnt = 0
    cakes = ('巧克力蛋糕', '檸檬蛋糕', '賭場蛋糕', '歌劇蛋糕', '草莓蛋糕', '松露蛋糕', '巧克力泡芙', '咖啡泡芙', '香草泡芙', '拿破崙蛋糕', '杏仁派', '蘋果派', '蘋果撻', '杏仁撻', '漿果撻', '黑莓撻', '藍莓撻', '巧克力撻', '櫻桃撻', '檸檬撻', '胡桃撻', '巧克力奶油餅乾', '剛果餅乾', '樹莓餅乾', '檸檬餅乾', '巧克力蛋白酥皮', '香草酥皮', '杏仁餅乾', '瓦片餅乾', '核桃餅乾', '杏仁果可頌', '蘋果可頌', '杏仁可頌', '奶酪可頌', '巧克力可頌', '杏仁丹麥麵包', '蘋果丹麥麵包', '杏仁果捲', '杏仁果熊爪糕', '藍莓丹麥麵包', '檸檬水', '覆盆子檸檬水', '橙汁', '綠茶', '瓶裝水', '熱咖啡', '巧克力咖啡', '香草星冰樂', '櫻桃蘇打', '義式濃縮咖啡')

    for i in data:
        no, *quantity = i.split(',')

        quantity = [int(q) for q in quantity]

        for d in range(50):
            items[d] += quantity[d]

        # if sum(quantity[-10:]) > 0:
        #     cnt += 1
        buy5 = [1 if q>=5 else 0 for q in quantity]
        if sum(buy5) >= 2:
            cnt+=1

        temp.append(f'{no:>5}: 購買{sum(quantity):>3}個\n')

    temp[-1] = temp[-1].strip()
    outfile.writelines(temp)

    for i in range(50):
        print(cakes[i],items[i])
    print(f'總計:{cnt}')