from math import inf 

class Node:
    def __init__(self, value, cordinates, neighbors=None):
        self.value = value
        self.x = cordinates[0]
        self.y = cordinates[1]
        self.heuristic_value = -1
        self.distance_from_start = inf
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
        self.parent = None

    def has_neighbors(self):
        if len(self.neighbors) == 0:
            return False
        return True

    def number_of_neighbors(self):
        return len(self.neighbors)

    def add_neighboor(self, neighboor):
        self.neighbors.append(neighboor)

    def extend_node(self):
        children = []
        for child in self.neighbors:
            children.append(child[0])
        return children
    
    def __gt__(self, other):
        if isinstance(other, Node):
            if self.heuristic_value > other.heuristic_value:
                return True
            if self.heuristic_value < other.heuristic_value:
                return False
            return self.value > other.value

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return self.value == other

    def __str__(self):
        return self.value
        

class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def add_node(self, node):
        self.nodes.append(node)

    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node 
        return None

    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)        
        node2 = self.find_node(value2)

        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor((node2, weight))
            #node2.add_neighboor((node1, weight))
        else:
            print("Error: One or more nodes were not found")

    def number_of_nodes(self):
        return f"The graph has {len(self.nodes)} nodes"

    def are_connected(self, node_one, node_two):
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)

        for neighboor in node_one.neighbors:
            if neighboor[0].value == node_two.value:
                return True
        return False

    def __str__(self):
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n" 
        return graph
