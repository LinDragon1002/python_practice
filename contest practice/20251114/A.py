from collections import defaultdict,deque
def bfs(tree,start_node):
    queue = deque([start_node])
    while queue:
        now_node = queue.popleft()
        print(now_node,end=" ")
        for next_node in tree[now_node]:
            queue.append(next_node)

tree=defaultdict(list)
root = ""
while True:
    try:
        no, *nos = input().split(' ')
        if root == "":
            root = no
        tree[no].extend(nos)
    except:
        break
bfs(tree,root)