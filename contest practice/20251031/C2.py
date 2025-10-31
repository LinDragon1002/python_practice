import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict

def dfs(Tree, now_node,depth):
    depths[now_node] = depth
    height = 0
    for next_node in Tree[now_node]:
        height = max(dfs(Tree,next_node,depth+1),height)
    heights[now_node] = height
    return height + 1

tree = defaultdict(list)
n = int(input())
parent = [-1] * n
depths = [0] * n
heights = [0] * n
for _ in range(n):
    id,k,*c = map(int,input().split())
    for i in c:
        parent[i] = id
    tree[id].extend(sorted(c))

root = parent.index(-1)
dfs(tree,root,0)

for id in range(n):
    types = ""
    if parent[id] == -1:
        types = "root"
    elif len(tree[id]) > 0:
        types = "internal node"
    else:
        types = "leaf"
    print(f"node {id}: parent = {parent[id]}, depth = {depths[id]}, height = {heights[id]}, {types}, {tree[id]}")
