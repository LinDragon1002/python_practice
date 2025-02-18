# c = int(input('請輸入成本:'))
# d = int(input('請輸入殘值:'))
# n = int(input('輸入年限:'))
# a = input('請輸入折舊方法:1.直線法 2.定率法 3.合計法 4.倍數法:')
# b=[]
# for i in a:
#     b.append(int(i))
# Y=list(range(1,n+1))
# A=[]
# B=[]
# C=[]
# D=[]
# if 1 or 2 or 3 or 4 in b:
#         if 1 in b:
#             for i in range(1, n + 1):
#                 z = int(round((c - d)/n,2))
#                 A.append(z)
#         if 2 in b:
#             for ii in range(0,n):
#                 R= 1 - ((d / c) ** (1 / n))
#                 z = int(round((c*(1-R)**ii)*R,2))
#                 B.append(z)
#         if 3 in b:
#             total = sum(range(1, n + 1))
#             for iii in range(0,n):
#                 z = int(round((c-d)*(n-iii)/total,2))
#                 C.append(z)
#         if 4 in b:
#             for iiii in range(0,n):
#                 R= (2/n)
#                 z = int(round((c*(1-R)**iiii)*R,2))
#                 D.append(z)

# print(f"{'方法順序':<10}{'直線':>2.5}{'變率':>8}{'年數':>8}{'倍數':>8}")  # 打印標題 問GPT
# for i in range(n):  # 假設每個列表長度相同
#     yy=Y[i] if i < len(Y) else ""
#     M = A[i] if i < len(A) else ""
#     N = B[i] if i < len(B) else ""
#     O = C[i] if i < len(C) else ""
#     P = D[i] if i < len(D) else ""
#     print(f"第{yy}年{M:>10}{N:>10}{O:>10}{P:>10}")


def straight_line(c, d, n):
    """直線法計算折舊"""
    return [int(round((c - d) / n, 2)) for _ in range(n)]

def declining_balance(c, d, n):
    """定律遞減法計算折舊"""
    R = 1 - ((d / c) ** (1 / n))
    return [int(round((c * (1 - R) ** i) * R, 2)) for i in range(n)]

def sum_of_years(c, d, n):
    """年數合計法計算折舊"""
    total = sum(range(1, n + 1))
    return [int(round((c - d) * (n - i) / total, 2)) for i in range(n)]

def double_declining(c, d, n):
    """倍數遞減法計算折舊"""
    R = 2 / n
    return [int(round((c * (1 - R) ** i) * R, 2)) for i in range(n)]

# 方法映射表
method_map = {
    '1': ("直線法", straight_line),
    '2': ("定律法", declining_balance),
    '3': ("年數法", sum_of_years),
    '4': ("倍數法", double_declining),
}

# 輸入
c, d, n, method = map(int, input("成本,殘值,耐用年限,樹入折舊方法 1直線法 2定律遞減法 3年數合計法 4倍數遞減法 eg:兩個方法輸入12 : ").split(','))

# 儲存使用的方法和計算結果
now_methods = []
all_results = []

# 處理每個方法
for m in str(method):
    if m in method_map:
        method_name, method_func = method_map[m]
        now_methods.append(method_name)
        all_results.append(method_func(c, d, n))

# 輸出表頭
print(f"{'方法順序':<3}", end="")
for method_name in now_methods:
    print(f"{method_name:>6}", end="")
print()

# 輸出報表內容
for year in range(n):
    print(f"第{year + 1}年", end="")
    for result in all_results:
        print(f"{result[year]:>10}", end="")
    print()
