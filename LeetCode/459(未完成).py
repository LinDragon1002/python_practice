s = "abababab"
if len(s) % 2 != 0:
    print(False)
else:
    # from typing import Counter
    # temp = list(Counter(s).values())
    temp = "".join(list(set(s)))
    if s.count(temp) * len(temp) == len(s):
        print(True)
    else:
        print(False)
    print(s.count(temp))

    # for i in range(len(temp)):
    #     if temp[i] % 2 != 0 and temp.count(temp[i]) % 2 != 0:
    #         print(False)
    # else:
    #     print(True)
