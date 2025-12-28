import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import defaultdict

def dfs(Tree, now_node):
    count = 0
    for next_node in Tree[now_node]:
        count += dfs(Tree,next_node)
        count += 1
    counts[now_node-1] = count
    return count

def dfs_copy(Tree, now_node):
    count = len(Tree[now_node])
    for next_node in Tree.get(now_node,[]):
        count += dfs_copy(Tree,next_node)
    counts[now_node-1] = count
    return count

tree = defaultdict(list)
num = int(input())
counts = [0] * num
top_number = list(map(int,input().split()))
for  i in range(1,num):
    tree[top_number[i-1]].append(i+1)

dfs_copy(tree,1)

print(*counts)