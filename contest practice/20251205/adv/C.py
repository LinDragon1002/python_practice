from typing import Counter
cases = 0
while True:
    try:
        cases += 1
        n = int(input())
        ans = 0
        for i in range(n):
            st = input()
            temp = list(Counter(st).values())
            if len(temp) >= 2 and  len(set(temp)) == len(temp):
                ans += 1
        print(f"Case {cases}: {ans}")
    except:
        break