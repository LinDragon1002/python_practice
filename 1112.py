with open('ntub.csv', 'r', encoding='utf-8') as infile:
    data = infile.readlines()

    data = [k.strip() for k in data]

    m_cnt = 0
    f_cnt = 0

    cnt = {}
    # cnt['男'] = 0
    # cnt['女'] = 0

    for i in data:

        gender, *_  = i.split(',')

        #方法一
        if gender == '男':
            m_cnt+=1
        if gender == '女':
            f_cnt+=1

        #方法二
        # cnt[gender]+=1

        #方法三
        if gender in cnt:
            cnt[gender]+=1
        else:
          cnt[gender]=1

    print(cnt)
    print(f'男:{cnt["男"]}人,女:{cnt["女"]}人')
    print(cnt.items())



cnt = {'女': 260, '男': 89}

#由小到大
cnt2 = sorted(cnt)
print(cnt2)

#由大到小
cnt2 = sorted(cnt, reverse=True)
print(cnt2)

#將dict內容轉成list
cnt3 = cnt.items()
print(cnt3)

#排序
cnt4 = sorted(cnt.items(), key= lambda x:x[1])
print(cnt4)



with open('ntub.csv', 'r', encoding='utf-8') as infile:
    data = infile.readlines()
    data = [k.strip() for k in data]
    cnt = {}

    for i in data:
        *_,chi,eng,math,_,_= i.split(',')
        total = int(chi)+int(eng)+int(math)
        if total in cnt:
            cnt[total]+=1
        else:
            cnt[total]=1

        cnt1 = sorted(cnt.items(), key= lambda x:(x[1], x[0]), reverse=True)
        cnt2 = sorted(cnt.items(), key= lambda x:(x[1], -x[0]), reverse=True)

    print(cnt1)
    print(cnt2)


with open('ntub.csv', 'r', encoding='utf-8') as infile:
    data = infile.readlines()
    data = [k.strip() for k in data]
    cnt = set()

    for i in data:
        *_,chi,eng,math,_,_= i.split(',')
        total = int(chi)+int(eng)+int(math)

        cnt.add(total)

    print(cnt)
    print(len(cnt))
    print(max(cnt))
    print(min(cnt))




with open('ntub.csv', 'r', encoding='utf-8') as infile:
    data = infile.readlines()
    data = [k.strip() for k in data]

    tot = {}
    cnt = {}

    for i in data:
        gender,_,_,_,chi,*_ = i.split(',')

        if gender not in cnt:
            cnt[gender] = 1
            tot[gender] = int(chi)
        else:
            cnt[gender]+=1
            tot[gender]+=int(chi)

    print(tot)
    print(cnt)
    for key in cnt:
        print(f'{key},{tot[key]/cnt[key]:.2f}')



with open('ntub.csv', 'r', encoding='utf-8') as infile:
    data = infile.readlines()
    data = [k.strip() for k in data]

    tot = {}
    cnt = {}

    for i in data:
        _,_,settype,_,_,eng,*_ = i.split(',')

        if settype not in cnt:
            cnt[settype] = 1
            tot[settype] = int(eng)
        else:
            cnt[settype]+=1
            tot[settype]+=int(eng)
        # cnt1 = sorted(cnt.items(),key=lambda x:x[1])

    for key in cnt:
        print(f'{key}共{cnt[key]}人,英文平均{tot[key]/cnt[key]:.2f}')


with open('ntub.csv', 'r', encoding='utf-8') as infile:
    data = infile.readlines()
    data = [k.strip() for k in data]
    data1 = ["英文不到10分","英文10~19分","英文20~29分","英文30~39分","英文40~49分","英文50~59分","英文60分"]
    cnt = {}

    for i in data:
        _,_,_,_,_,eng,*_ = i.split(',')

        ans = int(eng)//10

        if  data1[ans] not in cnt:
            cnt[data1[ans]] = 1
        else:
            cnt[data1[ans]]+=1
    print(cnt)
