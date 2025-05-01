def dfs_pre(T, index):
    n = len(T)
    left = index * 2 + 1
    right = index * 2 + 2
    print(T[index], end=" ")
    if left < n:
        dfs_pre(T, left)
    if right < n:
        dfs_pre(T, right)
T = input().split()
dfs_pre(T, 0)