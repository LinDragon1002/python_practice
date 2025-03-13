def thesame():
    st = input()
    while True:
        number = 1
        for i in range(len(st)-1):
            if st[i] == st[i+1]:
                st = st.replace(f'{st[i]}{st[i+1]}',"")
                number = 0
                break
            else:
                number += 1
        if number == len(st):
            break
    return st
print(thesame())