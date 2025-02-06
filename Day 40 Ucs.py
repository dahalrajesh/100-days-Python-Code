import heapq
from collections import deque

# Uniform Cost Search (UCS) for Weighted Graphs
def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [])]  # (cost, node, path)
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == goal:
            return cost, path, len(visited)  # Return cost, path, and explored nodes count

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return None, None, len(visited)

# Breadth-First Search (BFS) for Unweighted Graphs
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, len(visited)  # Return path and explored nodes count

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, len(visited)

# Example Weighted Graph (Adjacency List)
graph_weighted = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 10)],
    'C': [('A', 2), ('D', 3)],
    'D': [('B', 10), ('C', 3), ('E', 8)],
    'E': [('D', 8)]
}

# Example Unweighted Graph (Same structure but without weights)
graph_unweighted = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# Test with start = 'A' and goal = 'E'
ucs_cost, ucs_path, ucs_explored = uniform_cost_search(graph_weighted, 'A', 'E')
bfs_path, bfs_explored = bfs(graph_unweighted, 'A', 'E')

# Output Results
print(f"🔹 UCS: Cost = {ucs_cost}, Path = {' -> '.join(ucs_path)}, Nodes Explored = {ucs_explored}")
print(f"🔹 BFS: Path = {' -> '.join(bfs_path)}, Nodes Explored = {bfs_explored}")
