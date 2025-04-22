st = input()
ans = []
if st[0] == "#":
    for i in range(1,len(st),2):
        ans.append(int(st[i:i+2],16))
    print(f"rgb({ans[0]},{ans[1]},{ans[2]})")
else:
    st = st.replace("rgb(", "").replace(")", "")
    st = st.split(",")
    for i in st:
        if format(int(i), "0x").upper() == "0":
            ans.append("00")
        else:
            ans.append(format(int(i), "0x").upper())
    print(f"#{ans[0]}{ans[1]}{ans[2]}")