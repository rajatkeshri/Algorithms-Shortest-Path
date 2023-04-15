def dfs_path_search(graph, start, dest):
    """Performs Depth First Search on the provided graph, from start node to destination node.

    Args:
        graph (dict): An adjacency list representation of the graph
        start (char): Node from which the search should start
        dest (char): The destination node to be reached

    Returns:
        tuple: path from the start to destination and the path cost
    """
    # stack data structure which is used to store the neighbors of a node
    stk_ds = [(start, [start], 0)]

    # set data structure to keep track of all visited nodes
    visited_set = set()


    while stk_ds:
        # pop the most recent node pushed into the stack
        node, path, path_cost = stk_ds.pop()

        # checking popped node is destination node or not. If so, return the path and path cost
        if node == dest:
            return path,path_cost

        # adding the node to the visited set
        visited_set.add(node)

        # each neighboring node is checked if its visited or not. If not, it is added into
        # with updated path cost
        for neighbor, weight in sorted(graph[node].items()):
            if neighbor not in visited_set:
                stk_ds.append((neighbor, path + [neighbor], path_cost + weight))

    return None

if __name__ == '__main__':

    # adjacency list representation of the graph
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

    # returned path and its cost from the bfs_path_search method
    path, cost = dfs_path_search(robot_path_graph,'S','T')
    print('Path Found: {} Cost: {}'.format(path,cost))
