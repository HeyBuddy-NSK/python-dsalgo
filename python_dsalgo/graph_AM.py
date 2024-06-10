class GraphMatrix:
    def __init__(self,num_vertices):
        """
        Graph Adjacency Matrix Implementation
        """

        self.V = num_vertices
        
        # creating 2D list (matrix) with zeros
        self.graph = [[0]* num_vertices for _ in range(num_vertices)]
        
    def add_edge(self, u, v):
        """
        Adds the edges in graph.
        """
        #adding the edge from u to v
        self.graph[u][v] = 1
        
        # adding the edge from v to u for undirected graph
        self.graph[v][u] = 1
        
    def print_graph(self):
        """
        prints the adjacency matrix representation of graph.
        """

        for row in self.graph:
            print(" ".join(map(str, row)))    