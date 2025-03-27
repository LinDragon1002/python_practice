from typing import Counter

st = input()
number = st.count(',')
st = [i for i in st.replace(",","")]
temp = Counter(st)
cnt = 0
for i in temp:
    if temp[i] % number+1 == 0:
        cnt += 1
if cnt == len(temp):
    print(1)
else:
    print(0)