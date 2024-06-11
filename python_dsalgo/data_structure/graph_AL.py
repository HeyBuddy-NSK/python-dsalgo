
class GraphAL:
    def __init__(self):
        """
        Graph Adjacency List Implementation 
        """
        self.graph = {}
    
    def add_edge(self,u,v):
        """
        Addes edge in graph
        """
        
        # adding the edge from u to v
        if u not in self.graph:
            self.graph[u] = []
            
        self.graph[u].append(v)
        
        # adding the edge from v to u for undirected graph.
        if v not in self.graph:
            self.graph[v] = []
            
        self.graph[v].append(u)
        
    def print_graph(self):
        """
         prints adjacency list representation of graph.
        """
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")