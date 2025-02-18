import math
with open ('cake.csv','r') as infile, open ('out.csv','w',encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [i.strip() for i in data]

    temp = []
    items = [0] * 50
    cnt = 0
    cakes = ('巧克力蛋糕', '檸檬蛋糕', '賭場蛋糕', '歌劇蛋糕', '草莓蛋糕', '松露蛋糕', '巧克力泡芙', '咖啡泡芙', '香草泡芙', '拿破崙蛋糕', '杏仁派', '蘋果派', '蘋果撻', '杏仁撻', '漿果撻', '黑莓撻', '藍莓撻', '巧克力撻', '櫻桃撻', '檸檬撻', '胡桃撻', '巧克力奶油餅乾', '剛果餅乾', '樹莓餅乾', '檸檬餅乾', '巧克力蛋白酥皮', '香草酥皮', '杏仁餅乾', '瓦片餅乾', '核桃餅乾', '杏仁果可頌', '蘋果可頌', '杏仁可頌', '奶酪可頌', '巧克力可頌', '杏仁丹麥麵包', '蘋果丹麥麵包', '杏仁果捲', '杏仁果熊爪糕', '藍莓丹麥麵包', '檸檬水', '覆盆子檸檬水', '橙汁', '綠茶', '瓶裝水', '熱咖啡', '巧克力咖啡', '香草星冰樂', '櫻桃蘇打', '義式濃縮咖啡')

    for i in data:
        no, *quantity = i.split(',')

        quantity = [int(q) for q in quantity]

        for d in range(50):
            items[d] += quantity[d]

        if quantity[0] == quantity[46] and quantity[0] > 0 and quantity[46] > 0:
            cnt += 1

    print(f'總計:{cnt}')