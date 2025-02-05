from collections import deque

# Directions for movement (Down, Up, Right, Left)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(maze, start, end):
    """Finds the shortest path in a maze using BFS."""
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])  # Store (position, path taken)
    visited = set([start])
    nodes_explored = 0  # Count visited nodes

    while queue:
        (x, y), path = queue.popleft()
        nodes_explored += 1

        # If we reach the end, return the path and nodes explored
        if (x, y) == end:
            return path, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None, nodes_explored  # No path found


def dfs(maze, start, end):
    """Finds a valid path in a maze using DFS (not necessarily the shortest)."""
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]  # Store (position, path taken)
    visited = set([start])
    nodes_explored = 0  # Count visited nodes

    while stack:
        (x, y), path = stack.pop()
        nodes_explored += 1

        # If we reach the end, return the path and nodes explored
        if (x, y) == end:
            return path, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                stack.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None, nodes_explored  # No path found


# Example Maze (1 = walkable, 0 = wall)
maze = [
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

# Start and End Positions
start = (0, 0)
end = (4, 4)

# Solve using BFS
bfs_path, bfs_nodes = bfs(maze, start, end)
print(f"BFS Shortest Path: {bfs_path}")
print(f"BFS Nodes Explored: {bfs_nodes}")

# Solve using DFS
dfs_path, dfs_nodes = dfs(maze, start, end)
print(f"DFS Path Found: {dfs_path}")
print(f"DFS Nodes Explored: {dfs_nodes}")

# Compare BFS and DFS
print("\n🔹 Comparison:")
print(f"🔸 BFS explored {bfs_nodes} nodes.")
print(f"🔸 DFS explored {dfs_nodes} nodes.")
