import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Sample city graph (Intersections as nodes, roads as edges)
city_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F', 'G'],
    'F': ['C', 'E', 'H'],
    'G': ['E', 'H'],
    'H': ['F', 'G']
}


# 📌 Standard BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, len(visited)  # Return path and explored nodes

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, len(visited)


# 📌 Standard DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, len(visited)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, len(visited)


# 📌 Bi-Directional BFS
def bidirectional_bfs(graph, start, goal):
    if start == goal:
        return [start], 1

    front_queue = deque([(start, [start])])
    back_queue = deque([(goal, [goal])])

    front_visited = {start: [start]}
    back_visited = {goal: [goal]}

    while front_queue and back_queue:
        # Expand front search
        front_node, front_path = front_queue.popleft()
        for neighbor in graph.get(front_node, []):
            if neighbor not in front_visited:
                front_visited[neighbor] = front_path + [neighbor]
                front_queue.append((neighbor, front_path + [neighbor]))
                if neighbor in back_visited:
                    return front_visited[neighbor] + back_visited[neighbor][::-1][1:], len(front_visited) + len(
                        back_visited)

        # Expand back search
        back_node, back_path = back_queue.popleft()
        for neighbor in graph.get(back_node, []):
            if neighbor not in back_visited:
                back_visited[neighbor] = back_path + [neighbor]
                back_queue.append((neighbor, back_path + [neighbor]))
                if neighbor in front_visited:
                    return front_visited[neighbor] + back_visited[neighbor][::-1][1:], len(front_visited) + len(
                        back_visited)

    return None, len(front_visited) + len(back_visited)


# 📌 Visualizing the Graph using NetworkX
def draw_graph(graph, path=None):
    G = nx.Graph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 6))

    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", edge_color="gray", font_size=12)

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

    plt.show()


# 🔍 Test with start = 'A' and goal = 'H'
start, goal = 'A', 'H'
bfs_path, bfs_explored = bfs(city_graph, start, goal)
dfs_path, dfs_explored = dfs(city_graph, start, goal)
bi_bfs_path, bi_bfs_explored = bidirectional_bfs(city_graph, start, goal)

# 🔹 Print Results
print(f" BFS: Path = {' -> '.join(bfs_path)}, Nodes Explored = {bfs_explored}")
print(f" DFS: Path = {' -> '.join(dfs_path)}, Nodes Explored = {dfs_explored}")
print(f"Bi-Directional BFS: Path = {' -> '.join(bi_bfs_path)}, Nodes Explored = {bi_bfs_explored}")

#  Visualize the Shortest Path Found
draw_graph(city_graph, bi_bfs_path)
