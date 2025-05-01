def dfs_pre(T, index):
    n = len(T)
    left = index * 2 + 1
    right = index * 2 + 2
    if T[index] != "null":
        print(T[index], end=" ")
    if left < n:
        dfs_pre(T, left)
    if right < n:
        dfs_pre(T, right)
def dfs_in(T, index):
    n = len(T)
    left = index * 2 + 1
    right = index * 2 + 2
    if left < n:
        dfs_in(T, left)
    if T[index] != "null":
        print(T[index], end=" ")
    if right < n:
        dfs_in(T, right)
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
dfs_pre(T, 0)
print()
dfs_in(T, 0)
print()
dfs_post(T, 0)
