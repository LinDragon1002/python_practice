n = int(input())
for _ in range(n):
    st = input()
    check1 = st.count('(') != st.count(')')
    check2 = st.count('[') != st.count(']')
    if check1 or check2:
        print("No")
    else:
        Ans = "Yes"
        stack = []
        for s in st:
            # 只要 s 是左括號，放到堆疊
            if s in ['(','[']:
                stack.append(s)
            else:
                # 如果s是右括號，就取出堆疊最上方的元素(r)
                # 注意：如果這時候堆疊是空的，代表一定無法匹配，直接輸出No
                # 否則進行比對，是否 ( == ) or [ == ]
                if stack == []:
                    Ans = "No"
                    break
                r = stack.pop()
                if not(r == '(' and s == ')' or r == '[' and s == ']'):
                    Ans = "No"
                    break
        if stack != []:
            Ans = "No"
        print(Ans)

