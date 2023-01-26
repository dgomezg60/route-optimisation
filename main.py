from graph import Graph, Node
from a_star import AStar
from draw_graph import graphy
from mongodb import DataBase

def run(graph_data):
    # Create graph
    graph = Graph()
    
    # Add vertices
    for node in graph_data:
      graph.add_node(Node(node['Node'],(node['Position'][0],node['Position'][1])))

    # Add edges
    for node in graph_data:
      for edge in node['Edge']:
        graph.add_edge(node['Node'],edge['neightbour'],edge['weight'])

    # Execute the algorithm

    alg = AStar(graph, "B", "D")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")
    graphy_drawing = graphy()
    graphy_drawing.draw(graph_data)

if __name__ == '__main__':
    mongodb = DataBase()
    mongodb.loggin()
    mongodb.define_db('ruta','point')
    graph_data = mongodb.get_data()
    run(graph_data)
