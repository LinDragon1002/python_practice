from collections import defaultdict,deque

def bfs(Tree, start_node):
    queue = deque([start_node])
    while queue:
        now_node = queue.popleft()
        print(now_node,end=" ")
        for next_node in Tree[now_node]:
            queue.append(next_node)

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

bfs(tree,root)