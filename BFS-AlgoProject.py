from collections import deque


def bfs_shortest_path_robotics(graph, start, end):
    # All nodes visited
    visited = set()
    # Queue to manage traversal
    queue = deque([(start, [])])

    # Main BFS algorithm
    while queue:
        vertex, path = queue.popleft()
        # Check if T/end is reached now
        if vertex == end:
            return path + [vertex]
        # Skip node if already present in set
        if vertex in visited:
            continue
        # Mark node as visited
        visited.add(vertex)
        # Add all the neighboring vertices to the queue
        for neighbor, weight in graph[vertex].items():
            queue.append((neighbor, path + [vertex]))
    # No path found
    return None


def main():
    # Graph for the map-street positions
    robot_path_graph = {
        'S': {'C': 2.24, 'A':4.12, 'B': 9.61},
        'A': {'F': 2.24, 'S': 4.12},
        'B': {'D': 2, 'S': 9.61},
        'C': {'E': 2, 'S': 2.24},
        'D': {'F': 1.41, 'B': 2, 'E': 2},
        'E': {'C': 2, 'D': 2, 'I':6.08},
        'F': {'D': 1.41, 'A': 2.24, 'H':3},
        'H': {'I': 2, 'F': 3, 'J':3},
        'I': {'L':1, 'H': 2, 'E': 6.08},
        'J': {'M':1, 'H': 3, 'K': 3.16},
        'K': {'L': 2, 'J': 3.16},
        'L': {'I': 1, 'K': 2, 'N': 5},
        'M': {'T':1, 'J': 1, 'N': 2},
        'N': {'M': 2, 'T':2, 'L': 5},
        'T': {'M': 1, 'N': 2},

    }

    # Choose start and end vertices
    startingStreet = 'S'
    endingStreet = 'T'
    # Call the BFS shortest path function
    shortest_path = bfs_shortest_path_robotics(robot_path_graph, startingStreet, endingStreet)

    # Check the result and print the shortest path or a message if no path exists
    if shortest_path is not None:
        print(f"Shortest path from {startingStreet} to {endingStreet}: {' -> '.join(shortest_path)}")
    else:
        print(f"No path found from {startingStreet} to {endingStreet}")


# Call the main function if this script is being run as the entry point
if __name__ == '__main__':
    main()
