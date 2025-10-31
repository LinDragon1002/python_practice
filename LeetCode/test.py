def maxFreqSum(s: str) -> int:
    ans = 0
    vowels = {}
    consonants = {}
    for i in s:
        if i in ('a','e','i','o','u'):
            if i not in vowels:
                vowels[i] = 1
            else:
                vowels[i] +=1
        else:
            if i not in consonants:
                consonants[i] = 1
            else:
                consonants[i] += 1
    vowels = sorted(vowels.items(),key=lambda x:x[-1],reverse=True)
    consonants = sorted(consonants.items(),key=lambda x:x[-1],reverse=True)
    if len(vowels) > 0:
        ans += vowels[0][-1]
    if len(consonants) > 0:
        ans += consonants[0][-1]
    return ans
print(maxFreqSum('successes'))