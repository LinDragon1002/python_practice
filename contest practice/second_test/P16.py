st = [i for i in input()]

for i in range(len(st)):
    if st[i] != "(" and st[i] != ")":
        st[i] = "="
    elif st[i] == "(":
        st[i] = "?"
    elif st[i] == ")":
        for j in range(i,-1,-1):
            if st[j] == "?":
                st[i] = "*"
                st[j] = "*"
                break
        else:
            st[i] = "?"

print("".join(st))
