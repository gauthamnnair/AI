import heapq

def find_start_end(maze):
    start = end = None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return start, end

def construct_path(parent, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()  # Reverse the path to get from start to end
    return path

def dfs(maze):
    start, end = find_start_end(maze)
    stack = [start]
    visited = set()
    parent = {start: None}
    backtracked_path = []

    while stack:
        current = stack.pop()
        if current in visited:
            backtracked_path.append(current)
            continue
        visited.add(current)

        if current == end:
            break

        x, y = current
        neighbors = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        for neighbor in neighbors:
            nx, ny = neighbor
            if (0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and
                maze[ny][nx] in [' ', 'E'] and neighbor not in visited):
                stack.append(neighbor)
                parent[neighbor] = current

    final_path = construct_path(parent, start, end)
    return final_path, backtracked_path

def bfs(maze):
    start, end = find_start_end(maze)
    queue = [start]
    visited = set()
    parent = {start: None}
    backtracked_path = []

    while queue:
        current = queue.pop(0)
        if current in visited:
            backtracked_path.append(current)
            continue
        visited.add(current)

        if current == end:
            break

        x, y = current
        neighbors = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        for neighbor in neighbors:
            nx, ny = neighbor
            if (0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and
                maze[ny][nx] in [' ', 'E'] and neighbor not in visited):
                queue.append(neighbor)
                parent[neighbor] = current

    final_path = construct_path(parent, start, end)
    return final_path, backtracked_path

def a_star(maze):
    start, end = find_start_end(maze)
    open_set = []
    heapq.heappush(open_set, (0, start))
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    parent = {start: None}
    backtracked_path = []

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == end:
            return construct_path(parent, start, end), backtracked_path

        x, y = current
        neighbors = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        for neighbor in neighbors:
            nx, ny = neighbor
            if (0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and
                maze[ny][nx] in [' ', 'E']):
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
            else:
                backtracked_path.append(current)

    return [], backtracked_path

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance
