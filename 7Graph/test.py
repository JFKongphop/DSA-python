# Graph Exercise 1: Basic Graph
# Creating Graph by Adding Vertexs and Edges
# Finding Path using Simple Path: A path with no repeated vertices is called a simple path.
""" 
Reference: https://www.python-course.eu/graphs_python.php
"""

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    # Simple Path
    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None

    # All Simple Path
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

    graph = Graph(g)
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())

    print("\nAdd vertex:")
    graph.add_vertex("z")
    print("Vertices of graph:")
    print(graph.vertices())
    print("Adding an edge:")
    graph.add_edge({"a","z"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())

    print('\nAdding an edge:')
    graph.add_edge({"z","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())

    print('\nAdding an edge:')
    graph.add_edge({"d","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())   

    print('\nAdding an edge:')
    graph.add_edge({"d","e"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())  
    
    print('\nSTART PATH FROM VERTEX')
    print('The path from vertex "a" to vertex "b":')
    path = graph.find_path("a", "b")
    print(path)

    print('\nThe path from vertex "a" to vertex "f":')
    path = graph.find_path("a", "f")
    print(path)

    print('\nThe path from vertex "c" to vertex "c":')
    path = graph.find_path("c", "c")
    print(path)

    print('\nThe path from vertex "y" to vertex "b":')
    path = graph.find_path("y", "b")
    print(path)

    print('\nThe path from vertex "a" to vertex "c":')
    path = graph.find_path("a", "c")
    print(path)

    print('\nThe path from vertex "z" to vertex "e":')
    path = graph.find_path("z", "e")
    print(path)

    print('\nAll paths from vertex "y" to vertex "b":')
    path = graph.find_all_paths("y", "b")
    print(path)

    print('\nAll paths from vertex "a" to vertex "c":')
    path = graph.find_all_paths("a", "c")
    print(path)

    print('\nAll paths from vertex "z" to vertex "e":')
    path = graph.find_all_paths("z", "e")
    print(path)