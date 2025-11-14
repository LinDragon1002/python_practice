from collections import defaultdict,deque

def bfs(graph,start_node,prev_node):
    queue = deque()
    queue.append((start_node, prev_node))
    while queue:
        now_node, prev_node = queue.popleft()
        if move[now_node]  == False:
            prev[now_node] = prev_node
            if now_node == n:
                ans = []
                p = now_node
                ans.append(p)
                while True:
                    p = prev[p]
                    ans.append(p)
                    if p == 1:
                        print(len(ans))
                        print(*sorted(ans))
                        exit()

            move[now_node] = True
            for next_node in graph[now_node]:
                if move[next_node] == False:
                    queue.append((next_node, now_node))


graph = defaultdict(list)
n,m = map(int,input().split())
move = [False] * (n+1)
prev = [-1] * (n+1)
temp = 0
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs(graph,1,-1)
print("IMPOSSIBLE")
