import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_nearest_neighbor(neighbors, point):
    nearest = None
    min_distance = float('inf')

    for neighbor in neighbors:
        distance = euclidean_distance(neighbor, point)
        if distance < min_distance:
            min_distance = distance
            nearest = neighbor

    return nearest

# Example usage
neighbors = {(2, 3), (5, 1), (1, 8), (7, 4)}
point = (3, 3)

nearest_neighbor = find_nearest_neighbor(neighbors, point)
print(f"The nearest neighbor to {point} is {nearest_neighbor}")
