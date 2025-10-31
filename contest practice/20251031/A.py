from collections import defaultdict

def dfs(Tree, now_node):
    print(now_node, end=" ")
    for next_node in Tree[now_node]:
        dfs(Tree,next_node)


tree = defaultdict(list)
root = ""
while True:
    try:
        st, *sts = input().split()
        if root == "":
            root = st
        tree[st].extend(sts)
    except:
        break
dfs(tree,root)
