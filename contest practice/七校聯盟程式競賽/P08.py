def x():
    st = input()
    temp = st.count("*")
    temp1 = st.count("/")
    for i in range(temp):
        number = st.find("*")
        if st[number-1] != "X" and st[number+1] != "X":
            ans = int(st[number-1]) * int(st[number+1])
            st.removeprefix(f'{st[number-1]}*{st[number+1]}')
            st.removesuffix
        else:
            ans = st[number-1] + st[number+1]
    for i in range(temp1):
        number = st.find("/")
        if st[number-1] != "X" and st[number+1] != "X":
            ans = int(st[number-1]) // int(st[number+1])
        else:
            ans = st[number-1] + st[number+1]