import heapq

# Manhattan distance: sum of distances for all tiles
def manhattan_dis(state, goal):
    distance = 0
    for num in range(1, 9):  # Check tiles 1 through 8 (excluding 0)
        x1, y1 = divmod(state.index(num), 3)
        x2, y2 = divmod(goal.index(num), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Generate valid neighboring states by moving the blank tile (0)
def get_neighbor(state):
    neighbors = []
    idx = state.index(0)  # Find the blank tile
    row, col = divmod(idx, 3)

    # Possible moves: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))  # Convert back to tuple for immutability
    return neighbors

# A* Search Algorithm
def a_star(start, goal):
    queue = [(manhattan_dis(start, goal), 0, start, [])]  # (f, g, state, path)
    visited = set()

    while queue:
        f, g, current, path = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path + [current], len(visited)

        for neighbor in get_neighbor(current):
            if neighbor not in visited:
                heapq.heappush(queue, (manhattan_dis(neighbor, goal) + g + 1, g + 1, neighbor, path + [current]))
    
    return None, len(visited)

# Start and goal states
start = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Solved state
goal = (1, 2, 3, 4, 5, 6, 7, 0, 8)   # One move away from solved

# Run A* search
path, visited = a_star(start, goal)

# Output results
if path:
    print(f"Solved in {len(path) - 1} moves!")
    for state in path:
        print(state[:3], '\n', state[3:6], '\n', state[6:], '\n')
else:
    print("No solution found.")

print(f"Nodes explored: {visited}")
