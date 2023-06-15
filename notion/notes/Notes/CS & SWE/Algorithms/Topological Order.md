# Topological Order

- Reverse (topological) order
    
    It refers to the ordering of the nodes in a directed acyclic graph (DAG) in such a way that for any directed edge (u, v), where u comes before v in the ordering, v must come before u  [tail to head]
    
    The regular topological sorting algorithm assigns a unique number to each node in the DAG such that for every directed edge (u, v), u receives a smaller number than v. The nodes are then visited in ascending order of these numbers.
    
    To obtain the reverse topological order, you can perform the topological sorting algorithm and store the nodes in a list or a stack as they are visited. Once the algorithm completes, you can simply reverse the list or pop the elements from the stack to obtain the reverse topological order.
    
    ```python
    def reverse_topological_sort(graph):
        visited = set()
        stack = []
    
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)
    
        for node in graph:
            if node not in visited:
                dfs(node)
    
        return stack[::-1]  # Reversing the stack to get the reverse order
    
    # Example usage w/ adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D', 'E'],
        'D': ['F'],
        'E': [],
        'F': []
    }
    
    reverse_order = reverse_topological_sort(graph)
    print(reverse_order)
    ```
    
    The output of the above code will be: `['F', 'D', 'E', 'C', 'B', 'A']`, which represents the reverse topological order of the given DAG.
    
    - Why reverse topological instead of topological?
        
        SUMMARY: Make sure TAIL is processed before HEAD
        
        1. Dependency Resolution: In certain scenarios, you might need to process nodes in a way that satisfies their dependencies. Reverse topological order is useful when you want to process nodes in a way that ensures all dependencies of a node have already been processed before processing the node itself. This is common in build systems, task scheduling, and dependency resolution algorithms.
        2. Post-processing or Cleanup: Sometimes, you may need to perform post-processing or cleanup tasks on nodes after they have been processed. Reverse topological order allows you to perform such operations in a way that ensures that any cleanup or post-processing for a node is done after its dependencies have already been processed.
        3. Bottom-Up Analysis: Reverse topological order is suitable for bottom-up analysis of a directed acyclic graph. It allows you to propagate information or perform calculations from the leaves (nodes with no outgoing edges) to the roots (nodes with no incoming edges) of the graph. This can be useful in scenarios such as evaluating expressions, calculating dependencies, or performing optimizations.