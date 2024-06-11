def dfs(graph, start):
    """
    Perform an iterative Depth-First Search on the graph starting from the given node.

    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.
    start: The starting node for DFS.

    Returns:
    list: A list of nodes in the order they were visited.
    """
    visited = set()  # Set to keep track of visited nodes
    stack = [start]  # Initialize a list as a stack with the starting node
    order = []  # List to store the order of visited nodes

    while stack:
        node = stack.pop()  # Pop a node from the top of the stack
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            order.append(node)  # Add the node to the order list

            # Push all adjacent nodes that haven't been visited to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order
