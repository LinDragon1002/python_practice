from collections import deque

def solve_maze(maze_input):
    # 解析輸入，將每行字串轉換為列表
    maze = []
    start = None
    end = None

    for r, row_str in enumerate(maze_input):
        row = []
        for c, char in enumerate(row_str):
            if char == 'S':
                start = (r, c)
                row.append(0)  # S視為可通行
            elif char == 'E':
                end = (r, c)
                row.append(0)  # E視為可通行
            else:
                row.append(int(char))
        maze.append(row)

    # BFS 搜尋最短路徑
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == end:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                maze[nr][nc] == 0 and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1

# 讀取輸入並求解
maze_input = input().split(';')
result = solve_maze(maze_input)
print(1 if result != -1 else 0)


from collections import deque

def solve_maze(maze, start, rows, cols):
    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        x, y, dist = queue.popleft()

        # 拜訪的過程
        # for i in range(rows):
        #     for k in range(cols):
        #         if (x,y) == (i,k):
        #             print(f"*{maze[i][k]}*", end=" ")
        #         else:
        #             print(maze[i][k], end=" ")

        #     print()
        # print()
            
        for dr, dc in directions:
            nr, nc = x + dr, y + dc
            if (0 <= nr < rows and 0 <= nc < cols):
                if maze[nr][nc] == "E":
                    return 1
                if maze[nr][nc] == "0" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    return 0

maze = input().split(";")
rows, cols = len(maze), len(maze[0])
start = (0, 0)
for i in range(rows):
    for k in range(cols):
        if maze[i][k] == "S":
            start = (i, k)

print(solve_maze(maze, start, rows, cols))