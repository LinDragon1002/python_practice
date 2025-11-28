def dfs_post(T, index):
    n = len(T)
    left = index * 2 + 1
    right = index * 2 + 2
    if left < n:
        dfs_post(T, left)
    if right < n:
        dfs_post(T, right)
    if T[index] != "null":
        print(T[index], end=" ")

T = input().split()
dfs_post(T, 0)