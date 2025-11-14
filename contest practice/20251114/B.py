from collections import defaultdict,deque

def bfs(graph,start_node):
    queue = deque([start_node])
    while queue:
        now_node = queue.popleft()
        ans.append(now_node)
        print(now_node)
        for next_node in sorted(graph[now_node]):
            if next_node not in ans and next_node not in queue:
                queue.append(next_node)


graph = defaultdict(list)
num = int(input())
ans = []
while True:
    try:
        k1,k2 = map(int,input().split())
        graph[k1].append(k2)
        graph[k2].append(k1)
    except:
        break
bfs(graph,0)
