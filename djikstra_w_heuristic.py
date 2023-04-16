from astar import Graph, create_graph, add_heuristics
from collections import deque

heuristic_dic = {
    "S":14, "A":9, "B":10, "C":11, "D":11,
    "E":12, "F":9.5, "H":7, "I":8, "J":5, "K":6,
    "L":7, "M":1, "N":2, "T":0
    }

init_node = "S"
goal_node = "T"

def djikstra_heuristic(graph: Graph):
    # Create a queue
    # Push and pop from queue depending on the heuristic
    # Check if the goal i
    priority_queue = [(14, "S")]
    visited = []
    path = []
    path_cost = 0
    step = 0

    while len(priority_queue) > 0:
        step += 1
        print(f"Step {step}:")
        print("Path Cost: ", path_cost)
        print("Path: ", path)
        print("Visited: ", visited)
        # get highest priority element
        priority_queue = sort_highest_priority(priority_queue)
        print("Priority Queue: ", priority_queue)
        current_best_node = priority_queue.pop(0)
        print("Priority : ", current_best_node)
        current_node_name, current_node_path_cost = current_best_node[1], current_best_node[0]

        distance_from_previous = 0
        # update path cost
        if current_node_name != "S":
            # print("DISTANCE RETURN VALUE", graph.get_distance(current_best_node[1], path[-1][0]))
            distance_from_previous = graph.get_distance(current_best_node[1], path[-1][0])

        if distance_from_previous != -1:
            path_cost += distance_from_previous

            # mark as visited
            visited.append(current_node_name)
            path.append((current_node_name, path_cost))

            # check if goal state has been reached
            if current_node_name == goal_node:
                print("Goal node reached, stopping...")
                return path
            # get the neighbours
            adjacent_nodes = graph.get_adj_nodes(current_node_name)
            # get the distances
            # append it to the priority queue
            for node in adjacent_nodes:
                if node[1] not in visited:
                    priority_queue.append([path_cost + node[0] + graph.get_node_heuristic(node[1]), node[1]])



def sort_highest_priority(queue: list):
    return sorted(queue, key=lambda x: x[0])

def main():
    my_graph = create_graph()
    my_graph = add_heuristics(my_graph, heuristic_dic)
    print(my_graph.g)
    print(my_graph.h)

    answer_path = djikstra_heuristic(my_graph)
    print("Best path obtained:", answer_path)

if __name__ == "__main__":
    main()
