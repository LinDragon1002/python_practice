import sys
input = sys.stdin.readline

def find_palindromes_optimized(s):
    n = len(s)
    temp = len(set(s))
    palindromes = set()
    
    def expand_from_center(left, right):
        """從中心向兩邊擴展"""
        while left >= 0 and right < n and s[left] == s[right]:
            # 只記錄長度 > 1 的迴文
            if right - left + 1 > 1:
                palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    
    for i in range(n):
        # 奇數長度迴文 (中心是一個字元)
        expand_from_center(i, i)
        # 偶數長度迴文 (中心是兩個字元之間)
        expand_from_center(i, i + 1)
    
    return len(palindromes)+temp

while True:
    try:
        s = input()
        result = find_palindromes_optimized(s)
        print(f"The string '{s}' contains {result} palindromes.")
    except:
        break