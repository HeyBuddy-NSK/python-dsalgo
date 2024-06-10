def bfs(graph, start):
    """
    Perform a Breadth-First Search on the graph starting from the given node.

    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.
    start: The starting node for BFS.

    Returns:
    list: A list of nodes in the order they were visited.
    """
    visited = set()  # Set to keep track of visited nodes
    queue = [start]  # Initialize a list as a queue with the starting node
    order = []  # List to store the order of visited nodes

    while queue:
        node = queue.pop(0)  # Dequeue a node from the front of the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            order.append(node)  # Add the node to the order list
            
            # Enqueue all adjacent nodes that haven't been visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order
