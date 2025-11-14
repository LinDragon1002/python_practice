from collections import defaultdict
def dfs(Tree, now_node):
    height = 0
    for next_node in Tree[now_node]:
        height = max(dfs(Tree,next_node), height)
    heights[now_node-1] = height
    return height + 1

tree = defaultdict(list)
num = int(input())
heights = [0] * num
root = ""
for i in range(num-1):
    st, *sts = map(int,input().split())
    tree[st].extend(sts)
    if root == "":
        root = st
dfs(tree,root)

print(max(heights)+1)