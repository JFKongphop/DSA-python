# Graph Exercise 1: Basic Graph
# Creating Graph by Adding Vertexs and Edges
# Finding Path using Simple Path: A path with no repeated vertices is called a simple path.

class Graph(object):

    # create the graph by dict to collect the vertext and edges to connect together
    def __init__(self, graphDict = None) -> None:
        
        # check the dict is invalid
        if graphDict == None:
            graphDict = {}
        
        # set the graphDict to private object
        self.__graphDict = graphDict

    # return of all vetices (nodes) in graph 
    def vertices(self):

        # it contain in key dict is the head of all the vertices before connect the edges
        return list(self.__graphDict.keys())
    
    # return all of the edges between vertices 
    # it return by the vertices pair
    def edges(self):
        return self.__generateEdges()

    # add the vertex (node) in the graph and set the pair edge by empty list
    # it cannot duplicate vertex in graph
    def addVertex(self, vertex):
        if vertex not in self.__graphDict:
            # set vertex by key and value is empty list
            self.__graphDict[vertex] = []

    # add the age in to the graph 
    # check the vertex1 (main node) in graph
    # true => add vertex 2 in the vertex1 (key) by apped in list (value)
    # false => add vertex1 new (key) and vertex2 (value) in list
    def addEdge(self, edge):

        # check it not duplicate
        edge = set(edge)

        # # set to element to destructuring in tuple
        (vertex1, vertex2) = tuple(edge)

        # check the vertex1 (key) is valid
        if vertex1 in self.__graphDict:
            self.__graphDict[vertex1].append(vertex2)

        # key is invalid add new to graph (dict)
        else:
            self.__graphDict[vertex1] = [vertex2]

    # private method 
    # generate connecting each edge by pairing 
    # first access in vertices (key) by loop
    # second access in verties (values) in list by vertices (key) by loop again
    # third pairing {vertex (key), vertex (value)} but not duplicate
    # last add it to list by pairing element 
    def __generateEdges(self):

        # list of pairing edges
        edges = []

        # acess in each key to get vertex
        for vertex in self.__graphDict:

            # access in each value (list) by vertex key
            for neighbour in self.__graphDict[vertex]:

                # check is not duplicate
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
    
        return edges

    # convert the graph to return string
    def __str__(self):
        res = "vertices: "
        for k in self.__graphDict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generateEdges():
            res += str(edge) + " "
        return res

    # find the normal path (first or easiest path)
    # start vertex is first vertex of path
    # end vertex is target of the path want to find
    def findPath(self, startVertex, endVertex, path=None):
        
        # check the graph is valid
        if path == None:
            path = []
        
        # set the graph 
        graph = self.__graphDict
        
        # set the list to get the path in graph
        # recursive to add the vertex to this list 
        # 
        path = path + [startVertex]

        # if find itself return initial path 
        # then return when it equal of start
        if startVertex == endVertex:
            return path
        
        # if the start point is not in graph
        if startVertex not in graph:
            return None

        # find endVertex in list of startVertex (from graphDict vertex (key)) 
        for vertext in graph[startVertex]:

            # it stop when vertex in the list path is duplicate
            if vertext not in path:
                extendPath = self.findPath(vertext, endVertex, path)

                # found the duplicate vertex
                # end of the path
                if extendPath:
                    return extendPath
        
        # path or vertex is invalid or vertex is not have edge (not connect)
        return None
    
    # find all the path that can possible to go
    def findAllPaths(self, startVertex, endVertex, path = []):
        
        # set the graph 
        graph = self.__graphDict

        # add the path to when found for show
        path = path + [startVertex]

        # start and end is same vertex
        if startVertex == endVertex:
            return [path]

        # if start that not in graph
        if startVertex not in graph:
            return []

        # collect of all possible path
        paths = []

        # access in the vertex that connect with the startVertex path
        for vertext in graph[startVertex]:

            # find the path then it not in the edge
            if vertext not in path:
                
                # get all the paths by recursive of the path argument
                extendPaths = self.findAllPaths(vertext, endVertex, path)

                # collect the path that found
                for p in extendPaths:
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
    graph.addVertex("z")
    print("Vertices of graph:")
    print(graph.vertices())
    print("Adding an edge:")
    graph.addEdge({"a", "z"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())


    print('\nAdding an edge:')
    graph.addEdge({"z","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())


    print('\nAdding an edge:')
    graph.addEdge({"d","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())   


    print('\nAdding an edge:')
    graph.addEdge({"d","e"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())  


    print('\nSTART PATH FROM VERTEX')
    print('The path from vertex "a" to vertex "b":')
    path = graph.findPath("a", "b")
    print(path)

    print('\nThe path from vertex "a" to vertex "f":')
    path = graph.findPath("a", "f")
    print(path)

    print('\nThe path from vertex "c" to vertex "c":')
    path = graph.findPath("c", "c")
    print(path)

    print('\nThe path from vertex "y" to vertex "b":')
    path = graph.findPath("y", "b")
    print(path)

    print('\nThe path from vertex "a" to vertex "c":')
    path = graph.findPath("a", "c")
    print(path)

    print('\nThe path from vertex "z" to vertex "e":')
    path = graph.findPath("z", "e")
    print(path)

    print('\nAll paths from vertex "y" to vertex "b":')
    path = graph.findAllPaths("y", "b")
    print(path)

    print('\nAll paths from vertex "a" to vertex "c":')
    path = graph.findAllPaths("a", "c")
    print(path)

    print('\nAll paths from vertex "z" to vertex "e":')
    path = graph.findAllPaths("z", "e")
    print(path)