
class Graph:
    """
    Class Graph is used to define the given graph. 
    """
    def __init__(self):
        """
        intialize the graph
        initialize tej heuristic
        """
        self.g = {}
        self.h = {}

    def add_node(self, node, cost, adj_node):
        """
        function to add node to the graph
        graph - A -> [[2,B], [4,C]]
        params: 
            node: node name
            cost: edge cost 
            adj_node: adjacent node name
        """
        if node not in self.g:
            self.g[node] = []
        self.g[node].append([cost,adj_node])

    def get_adj_nodes(self, init_node):
        """
        function to get adj nodes given current node
        params:
            init_node: initial node
        return:
            adjacent nodes array
        """
        return self.g[init_node]
    
    def add_heuristic(self, node, h_value):
        """
        function to add heuristic to the graph
        params: 
            node: node name
            h_value: heuristic value for the node
        """
        if node not in self.h:
            self.h[node] = []
        self.h[node] = h_value

    def get_node_heuristic(self, node):
        """
        function to get adj nodes given current node
        params:
            node: node name
        return:
            heuristic for the given node
        """
        return self.h[node]
    
def create_graph():
    """
    function to create graph
    """
    # Creating the graph
    astar_graph = Graph()
    astar_graph.add_node("S", 4.12, "A")
    astar_graph.add_node("S", 9.61, "B")
    astar_graph.add_node("S", 2.24, "C")

    astar_graph.add_node("A", 4.12, "S")
    astar_graph.add_node("A", 2.24, "F")

    astar_graph.add_node("B", 9.61, "S")
    astar_graph.add_node("B", 2, "D")

    astar_graph.add_node("C", 2.24, "S")
    astar_graph.add_node("C", 2, "E")

    astar_graph.add_node("D", 2, "B")
    astar_graph.add_node("D", 2, "E")
    astar_graph.add_node("D", 1.41, "F")

    astar_graph.add_node("E", 2, "C")
    astar_graph.add_node("E", 2, "D")
    astar_graph.add_node("E", 6.08, "I")

    astar_graph.add_node("F", 1.41, "D")
    astar_graph.add_node("F", 3, "H")

    astar_graph.add_node("H", 3, "F")
    astar_graph.add_node("H", 2, "I")
    astar_graph.add_node("H", 3, "J")

    astar_graph.add_node("I", 2, "H")
    astar_graph.add_node("I", 6.08, "E")
    astar_graph.add_node("I", 1, "L")

    astar_graph.add_node("J", 3, "H")
    astar_graph.add_node("J", 3.16, "K")
    astar_graph.add_node("J", 1, "M")

    astar_graph.add_node("K", 3.16, "J")
    astar_graph.add_node("K", 2, "L")

    astar_graph.add_node("L", 2, "K")
    astar_graph.add_node("L", 1, "I")
    astar_graph.add_node("L", 5, "N")

    astar_graph.add_node("M", 1, "J")
    astar_graph.add_node("M", 2, "N")
    astar_graph.add_node("M", 1, "T")

    astar_graph.add_node("N", 5, "L")
    astar_graph.add_node("N", 2, "M")
    astar_graph.add_node("N", 2, "T")

    astar_graph.add_node("T", 1, "M")
    astar_graph.add_node("T", 2, "N")

    return astar_graph

def add_heuristics(astar_graph, heuristic_dic):
    """
    function to update heuristic to the graph
    params:
        astar_graph: graph object
        heuristic_dic: all heuristics
    """
    for i in heuristic_dic:
        astar_graph.add_heuristic(i, heuristic_dic[i])
    return astar_graph

#-------------------------------------------------------
# create graph and add heuristics
heuristic_dic = {
    "S":14, "A":9, "B":10, "C":11, "D":11,
    "E":12, "F":9.5, "H":7, "I":8, "J":5, "K":6, 
    "L":7, "M":1, "N":2, "T":0
    }

astar_graph = create_graph()
astar_graph = add_heuristics(astar_graph, heuristic_dic)

#-----------------------------
# find shortest path - A*

# initialize init node and final node
# initialize a queue and path to store final path
# initialize visited array to store all visited nodes
init_node = "S"
final_node = "T"
queue = []
queue.append([init_node,0])
path = []
visited = []

# looping until queue is empty
while len(queue)!=0:

    # pop first element in queue and check if its terminal
    q = queue.pop(0)
    node = q[0]
    value_until_now = q[1]
    
    #-------------------------------------
    print("Exploring Node ", node)
    #-------------------------------------

    path.append([node, value_until_now])
    if node == final_node:
        print("Node {} is destination ".format(node))
        print()
        break

    # if first element is not terminal, find adj nodes and add to queue
    adj_nodes = astar_graph.get_adj_nodes(node)
    
    #-------------------------------------
    print("Adj Nodes to {} = {} ".format(node, adj_nodes))
    #-------------------------------------

    #find node whose f=g+h is the most minimum and add to queue
    f_min = 1000000000
    f_node = ""
    for adj in adj_nodes:
        if adj[1] not in visited:
            print("Exploring adj node ", adj[1])
            print("f = g+h =", value_until_now + adj[0] + astar_graph.get_node_heuristic(adj[1]))

            if value_until_now + adj[0] + astar_graph.get_node_heuristic(adj[1]) < f_min:
                f_min = value_until_now + adj[0] + astar_graph.get_node_heuristic(adj[1])
                f_node = adj[1]
    
    #-------------------------------------
    print("Min Heuristic Adj Node =", f_node)
    print("Path Value till now =", value_until_now)
    print()
    #-------------------------------------

    # store new path cost until now 
    value_until_now = f_min-astar_graph.get_node_heuristic(f_node)
    queue.append([f_node, value_until_now])
    visited.append(f_node)

node_path = []
final_score = 0
for p in path:
    node_path.append(p[0])
final_score = path[-1][-1]

print("Shortest Path =", node_path)
print("Shortest path cost =", final_score)
print()








        