# Depth-First Search (DFS) Algorithm

def dfs(graph, node, visited=None):
    """
    Performs a Depth-First Search traversal on a graph starting from a given node.
    
    Args:
        graph: Dictionary representing the graph (adjacency list)
        node: Starting node for DFS
        visited: Set of visited nodes (default: None)
    
    Returns:
        List of nodes in DFS order
    """
    if visited is None:
        visited = set()
    
    visited.add(node)
    result = [node]
    
    # Visit all adjacent nodes
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph, start):
    """
    Iterative implementation of DFS using a stack.
    
    Args:
        graph: Dictionary representing the graph (adjacency list)
        start: Starting node for DFS
    
    Returns:
        List of nodes in DFS order
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add neighbors to stack (reverse order for correct DFS)
            stack.extend(reversed(graph.get(node, [])))
    
    return result


# Example usage
if __name__ == "__main__":
    # Create a sample graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Recursive DFS starting from 'A':")
    print(dfs(graph, 'A'))
    
    print("\nIterative DFS starting from 'A':")
    print(dfs_iterative(graph, 'A'))